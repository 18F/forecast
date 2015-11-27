import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from opportunities.models import Office, Opportunity
from optparse import make_option


# A data loader of contract opportunities
# Thank you Brendan Sudol... :)
# https://github.com/brendansudol/calc/blob/ca4a13d0fa34a468d788710975bf71959eb8bb20/contracts/management/commands/load_s70.py
class Command(BaseCommand):
    help = 'Load data from CSV'

    default_filename = 'forecast/fixtures/fy16q1.csv'

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
        self.stdout.write("Hello world!")
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
        print('begin loading task')

        opportunities = list(self.parse_file(filename, strict=strict))

        # self.insert(contracts, replace=replace)

    def parse_file(self, filename, strict=False):
        with open(filename, 'rU') as f:
            reader = csv.reader(f)

            for _ in range(self.header_rows):
                next(reader)

            count = skipped = 0
            for row in reader:
                try:
                    yield print(row)
                    # yield self.make_contract(row)
                    count += 1
                except (ValueError, ValidationError) as e:
                    if strict:
                        logger.error('error parsing {}'.format(row))
                        raise
                    else:
                        skipped += 1

    # @classmethod
    # def make_contract(cls, row):
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
    # @staticmethod
    # def parse_date(s):
    #     if not s:
    #         return None
    #
    #     month, day, year = list(map(int, s.split('/')))
    #     return date(year, month, day)
    #
    # @classmethod
    # def insert(cls, contracts, replace=True, update_search_field=True):
    #     with transaction.atomic():
    #         if replace:
    #             logger.info('erasing existing contracts')
    #             cls.model.objects.filter(schedule=cls.schedule_name).delete()
    #
    #         logger.info('inserting new contracts')
    #         cls.model.objects.bulk_create(contracts)
    #
    #     if update_search_field:
    #         logger.info('updating search field')
    #         call_command(
    #             'update_search_field',
    #             cls.model._meta.app_label,
    #             cls.model._meta.model_name
    #         )
