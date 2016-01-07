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
            '-a', '--append',
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
    )

    def handle(self, *args, **options):
        filename = options['filename']
        if not filename or not os.path.exists(filename):
            raise ValueError('invalid filename')

        OpportunitiesLoader().load(
            filename,
            replace=options['replace'],
            strict=options['strict']
        )


class OpportunitiesLoader(object):
    model = Opportunity
    header_rows = 1

    def load(self, filename, replace=True, strict=False):
        opportunities = list(self.parse_file(filename, strict=strict))

        self.insert(opportunities, replace=replace)

    def parse_file(self, filename, strict=False):
        with open(filename, 'rU') as f:
            reader = csv.reader(f)

            for _ in range(self.header_rows):
                next(reader)

            count = skipped = 0
            for row in reader:
                try:
                    yield self.make_opportunity(row)
                    count += 1
                except (ValueError, ValidationError) as e:
                    if strict:
                        print('error parsing {}'.format(row))
                        raise
                    else:
                        skipped += 1

    @classmethod
    def make_opportunity(cls, row):
        office = cls.insert_office(row[0], row[1])

        adv = cls.parse_advisor(row[23])
        advisor = cls.insert_advisor(adv[0], adv[1], adv[2])

        opportunity = cls.model(
            office=office,
            description=row[3],
            place_of_performance_city=row[4],
            place_of_performance_state=row[5],
            naics=row[6],
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
            estimated_fiscal_year=row[20].split("-")[0][3:],
            estimated_fiscal_year_quarter=int(row[20].split("-")[1][0]
                                                     .replace(r"Q", "0")),
            additional_information=row[24],
            published=True
        )
        return opportunity
    #     schedule = row[9]
    #     if schedule != cls.schedule_name:
    #         raise ValueError('skipping schedule: {}'.format(schedule))
    #
    #     price = row[5]
    #     if not price:
    #         raise ValueError('missing price')
    #
    #     price = cls.model.normalize_rate(price)
    #     display_price = price if price >= FEDERAL_MIN_CONTRACT_RATE else None
    #
    #     contract = cls.model(
    #         idv_piid=row[6],
    #         contract_start=cls.parse_date(row[12]),
    #         contract_end=cls.parse_date(row[13]),
    #         contract_year=cls.int_or_fallback(row[11], 1),
    #         vendor_name=row[7],
    #         price_min=row[X].replace("\$","").replace(",","")
    #         price_max=row[X].replace("\$","").replace(",","")
    #         labor_category=row[1].strip().replace('\n', ' '),
    #         education_level=cls.model.get_education_code(row[2]),
    #         min_years_experience=cls.int_or_fallback(row[3]),
    #         hourly_rate_year1=price,
    #         hourly_rate_year2=None,
    #         hourly_rate_year3=None,
    #         hourly_rate_year4=None,
    #         hourly_rate_year5=None,
    #         current_price=display_price,
    #         next_year_price=None,
    #         second_year_price=None,
    #         contractor_site=row[10],
    #         schedule=schedule,
    #         business_size=row[8],
    #         sin=row[0]
    #     )
    #
    #     contract.full_clean(exclude=['piid'])
    #
    #     return contract
    #
    # @staticmethod
    # def int_or_fallback(x, fallback=0):
    #     try:
    #         return int(x)
    #     except ValueError:
    #         return fallback
    #

    @staticmethod
    def parse_date(s):
        if not s or not re.match(r"\d{1,2}\/\d{1,2}\/\d{2,4}", s):
            return None
        month, day, year = list(map(int, s.split('/')))
        return date(year, month, day)

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
            return None

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
