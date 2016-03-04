import os
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
import re

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from django.db import transaction
from opportunities.models import Office, Opportunity, OSBUAdvisor
from optparse import make_option


# A data loader of contract opportunities
# Thank you Brendan Sudol... :)
# https://github.com/brendansudol/calc/blob/ca4a13d0fa34a468d788710975bf71959eb8bb20/contracts/management/commands/load_s70.py
# And converted by Dave Zvenyach at https://github.com/18F/forecast/blob/load-command/forecast-admin/forecast/opportunities/management/commands/load_opportunities.py
class Command(BaseCommand):
    help = 'Load data from CSV'

    default_filename = 'forecast/data/fy16q1.csv'

    option_list = BaseCommand.option_list + (
        make_option(
            '-f', '--filename',
            default=default_filename,
            help='input filename (.csv, default {})'.format(
                default_filename
            )
        ),
        make_option(
            '-p', '--append',
            dest='replace',
            action='store_false',
            default=True,
            help='Append data (default is to replace).'
        ),
        make_option(
            '-s', '--strict',
            action='store_true',
            default=False,
            help='Abort if any input data fails validation.'
        ),
        make_option(
            '-a', '--agency',
            default='GSA',
            action='store',
            # dest='agency',
            help='Set the agency name (default: GSA)'
        )
    )

    def handle(self, *args, **options):
        filename = options['filename']
        if not filename or not os.path.exists(filename):
            raise ValueError('invalid filename')

        OpportunitiesLoader().load(
            filename,
            replace=options['replace'],
            strict=options['strict'],
            agency=options['agency']
        )


class OpportunitiesLoader(object):
    model = Opportunity
    header_rows = 1

    def load(self, filename, replace=True, strict=False, agency='GSA'):
        opportunities = list(self.parse_file(filename, strict=strict, agency=agency))

        self.insert(opportunities, replace=replace)

    def parse_file(self, filename, strict=False, agency='GSA'):
        with open(filename, 'rU') as f:
            reader = csv.reader(f)

            for _ in range(self.header_rows):
                next(reader)

            count = skipped = 0
            for row in reader:
                try:
                    yield self.make_opportunity(row, agency)
                    count += 1
                except (ValueError, ValidationError) as e:
                    if strict:
                        print('error parsing {}'.format(row))
                        raise
                    else:
                        skipped += 1

    @classmethod
    def make_opportunity(cls, row, agency='GSA'):
        if agency in ["GSA","Education"]:
            office = cls.insert_office(row[0], row[1])

            adv = cls.parse_advisor(row[23])
            advisor = cls.insert_advisor(adv[0], adv[2], adv[1])

            fiscals = cls.parse_fiscal_dates(row[20])
            if agency == "Education":
                agency = "Dept. of Education"

            opportunity = cls.model(
                agency=agency,
                office=office,
                description=row[3],
                place_of_performance_city=row[4],
                place_of_performance_state=row[5],
                naics=cls.parse_socioeconomic(row[6]),
                socioeconomic=row[7],
                contract_type=row[8],
                procurement_method=row[9],
                competition_strategy=row[10],
                dollar_value_min=cls.parse_dollars(row[11]),
                dollar_value_max=cls.parse_dollars(row[12]),
                delivery_order_value=row[13],
                incumbent_name=row[14],
                new_requirement=row[16],
                funding_agency=row[17],
                estimated_solicitation_date=cls.parse_date(row[18]),
                fedbizopps_link=row[19],
                estimated_fiscal_year=fiscals[0],
                estimated_fiscal_year_quarter=fiscals[1],
                osbu_advisor=advisor,
                additional_information=row[24],
                published=True
            )
            return opportunity

        elif agency == "USAID":
            year = row[11][-4:].strip()

            opportunity = cls.model(
                agency=agency,
                description=row[2]+": "+row[3][0:800],
                place_of_performance_state=row[0],
                naics=cls.parse_socioeconomic(row[5]),
                procurement_method=row[8],
                competition_strategy=row[9],
                dollar_value_min=cls.parse_dollars_plus(row[6].split('-')[0]),
                dollar_value_max=cls.parse_dollars_plus(row[6].split('-')[1][1:]),
                delivery_order_value=row[6],
                new_requirement=row[15],
                funding_agency=row[4],
                estimated_solicitation_date=cls.parse_date(row[12]),
                estimated_fiscal_year=year,
                estimated_fiscal_year_quarter="TBD",
                point_of_contact_name=row[1],
                additional_information=row[13],
                published=True
            )
            # print(opportunity)
            return opportunity

        elif agency == "SSA":
            dollars = row[6].strip().split('and')

            opportunity = cls.model(
                agency=agency,
                description=row[1],
                place_of_performance_state=row[8],
                naics=cls.parse_socioeconomic(row[2]),
                contract_type=row[4],
                competition_strategy=row[5],
                dollar_value_min=cls.parse_dollars_plus(dollars[0]),
                incumbent_name=row[7],
                new_requirement=row[0],
                additional_information=row[9],
                published=True
            )
            if len(dollars) > 1:
                opportunity.dollar_value_max = cls.parse_dollars_plus(dollars[1])

            return opportunity

        elif agency == "Treasury":
            opportunity = cls.model(
                agency="Dept. of Treasury",
                # office=office,
                description=row[2],
                place_of_performance_city=row[10],
                place_of_performance_state=row[11],
                naics=cls.parse_socioeconomic(row[3]),
                contract_type=row[5],
                competition_strategy=row[6],
                incumbent_name=row[9],
                new_requirement=row[1],
                funding_agency=row[0],
                estimated_solicitation_date=cls.parse_date(row[14]),
                point_of_contact_name=row[12],
                point_of_contact_email=row[13],
                additional_information="End date: "+row[16],
                published=True
            )
            if len(row[15]) > 0:
                opportunity.estimated_fiscal_year=row[15][-4:]
            if not "TBD" in row[7]:
                dollars = row[7].strip().split('and')
                opportunity.dollar_value_min=cls.parse_dollars_plus(dollars[0])
                if len(dollars) > 1:
                    opportunity.dollar_value_max=cls.parse_dollars_plus(dollars[1])

            return opportunity

        elif agency == "State":
            office = cls.insert_office(row[2],"")

            opportunity = cls.model(
                agency="Dept. of State",
                office=office,
                description=row[1],
                naics=cls.parse_socioeconomic(row[4]),
                competition_strategy=row[5],
                incumbent_name=row[7],
                new_requirement=row[3],
                estimated_fiscal_year="20"+row[0][3:4],
                estimated_fiscal_year_quarter=cls.parse_fiscal_quarter_only(row[9]),
                point_of_contact_name=row[11],
                point_of_contact_email=row[12],
                published=True
            )
            if "and" in row[6]:
                dollars = row[6].strip().split('and')
                opportunity.dollar_value_min=cls.parse_dollars_plus(dollars[0])
                if len(dollars) > 1:
                    opportunity.dollar_value_max=cls.parse_dollars_plus(dollars[1])
            if len(row[10]) > 3:
                place_of_performance_state=row[3]
            return opportunity

    @staticmethod
    def parse_date(s):
        if not s or not re.match(r"^\d{1,2}\/\d{1,2}\/\d{2,4}$", s):
            return None
        month, day, year = list(map(int, s.split('/')))
        return date(year, month, day)

    @staticmethod
    def parse_fiscal_dates(s):
        try:
            split = s.split("-")
            year = split[0][3:]
            original_quarter = split[1]
            q = re.search(r"(\d)", original_quarter)
            if q:
                n = q.group(1)
                if n == "1":
                    quarter = "1st"
                elif n == "2":
                    quarter = "2nd"
                elif n == "3":
                    quarter = "3rd"
                elif n == "4":
                    quarter = "4th"
            else:
                quarter = "To Be Determined"
            return year, quarter
        except:
            return ["",""]

    @staticmethod
    def parse_fiscal_quarter_only(s):
        q = re.search(r"(\d)", s)
        if q:
            n = q.group(1)
            if n == "1":
                quarter = "1st"
            elif n == "2":
                quarter = "2nd"
            elif n == "3":
                quarter = "3rd"
            elif n == "4":
                quarter = "4th"
        else:
            quarter = "To Be Determined"
        return quarter

    @staticmethod
    def parse_dollars_plus(s):
        if "." in s:
            return re.sub(".","", s[1:]) + "0000"
        else:
            SUBS=[
                (" ",""),
                (r"[\$,\>\<\=\n]",""),
                ("M","000000"),
                ("K","000")
            ]
            parsed = s.strip()
            for pattern, replacement in SUBS:
                parsed = re.sub(pattern,replacement, parsed)
            return parsed

    @staticmethod
    def parse_dollars(s):
        try:
            amt = s.strip().replace("$", "").replace(",", "")
            return Decimal(amt)
        except:
            return None

    @staticmethod
    def parse_advisor(s):
        try:
            # Some entries have commas and some don't, so work around that
            # TODO: account for improper name formatting without miscapitalizing names
            split = s.replace(","," ").replace("  "," ").split(' ')
            adv = [' '.join(split[0:-2]), split[-2], split[-1]]
            return adv
        except:
            return [s,'','']

    @staticmethod
    def parse_socioeconomic(s):
        if len(s) == 6:
            return s
        else:
            return s[0:5]

    @classmethod
    def insert_office(cls, organization, region, replace=True):
        try:
            obj, created = Office.objects.update_or_create(
                organization=organization,
                region=region
            )
            return obj
        except ValueError:
            return False

    @classmethod
    def insert_advisor(cls, name, email, phone, replace=True):
        try:
            obj, created = OSBUAdvisor.objects.update_or_create(
                name=name,
                email=email,
                phone=phone
            )
            return obj
        except ValueError:
            return False

    @classmethod
    def insert(cls, opportunities, replace=True):
        with transaction.atomic():
            if replace:
                cls.model.objects.all().delete()
            cls.model.objects.bulk_create(opportunities)
