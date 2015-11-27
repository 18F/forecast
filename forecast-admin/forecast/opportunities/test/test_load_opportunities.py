import os

from collections import OrderedDict
from django.core.management import call_command
from django.test import TestCase

from opportunities.management.commands.load_opportunities import (
    OpportunitiesLoader
)
from opportunities.models import Opportunity


class LoadOpportunitiesTestCase(TestCase):
    sample_filename = 'data/s70_sample.csv'
    bad_filename = 'data/s70_bad_sample.csv'
    empty_filename = 'data/s70_empty.csv'

    def load(self, filename, **kwargs):
        call_command(
            'load_opportunities',
            filename=os.path.join(os.path.dirname(__file__), filename),
            verbosity=0,
            **kwargs
        )

    # def make_initial_data(self, quantity):
    #     recipe = get_contract_recipe(schedule=Schedule70Loader.schedule_name)
    #     return recipe.make(_quantity=quantity)
    #
    # def test_clears_initial(self):
    #     self.make_initial_data(10)
    #     self.assertEquals(Contract.objects.count(), 10)
    #
    #     self.load(self.empty_filename)
    #     self.assertEquals(Contract.objects.count(), 0)
    #
    # def test_loads_sample(self):
    #     self.load(self.sample_filename)
    #     self.assertEquals(Contract.objects.count(), 20)
    #
    # def test_loads_bad_sample_and_warns(self):
    #     output = self.load(self.bad_filename)
    #     self.assertEquals(Contract.objects.count(), 18)
    #
    # def test_strict_mode_fails(self):
    #     self.assertRaises(
    #         ValueError,
    #         self.load,
    #         self.bad_filename,
    #         strict=True
    #     )
    #
    # def test_failure_doesnt_erase_existing_data(self):
    #     self.make_initial_data(3)
    #     self.assertEquals(Contract.objects.count(), 3)
    #
    #     try:
    #         self.load(self.bad_filename, strict=True)
    #     except ValueError:
    #         self.assertEquals(Contract.objects.count(), 3)
    #
    # def test_int_or_fallback(self):
    #     int_or_fallback = Schedule70Loader.int_or_fallback
    #     self.assertEquals(int_or_fallback('123'), 123)
    #     self.assertEquals(int_or_fallback(456), 456)
    #     self.assertEquals(int_or_fallback('foo'), 0)
    #     self.assertEquals(int_or_fallback('43.3', 1), 1)
    #
    # def test_parse_date(self):
    #     parse_date = Schedule70Loader.parse_date
    #     self.assertEquals(parse_date('12/8/2015'), date(2015, 12, 8))
    #     self.assertEquals(parse_date('06/03/2014'), date(2014, 6, 3))
    #
    # def make_row(self, **kwargs):
    #     default = OrderedDict([
    #         ('sin', '123-45'),
    #         ('labor_category', 'Tester'),
    #         ('education_level', 'Bachelors'),
    #         ('min_years_experience', 5),
    #         ('unit', 'hour'),
    #         ('price', '123.45'),
    #         ('contract_number', 'GS-12A-345BC'),
    #         ('company_name', '18F'),
    #         ('business_size', 'S'),
    #         ('schedule', Schedule70Loader.schedule_name),
    #         ('location', 'both'),
    #         ('current_year', 1),
    #         ('begin_date', '1/12/13'),
    #         ('end_date', '12/1/17'),
    #     ])
    #
    #     return [kwargs.get(k, v) for k, v in default.items()]
    #
    # def test_make_contract_ok(self):
    #     Schedule70Loader.make_contract(self.make_row())
    #
    # def test_make_contract_no_price(self):
    #     row_no_price = self.make_row(price=None)
    #     self.assertRaises(
    #         ValueError,
    #         Schedule70Loader.make_contract,
    #         row_no_price
    #     )
    #
    # def test_make_contract_wrong_schedule(self):
    #     row_wrong_schedule = self.make_row(schedule='foobar')
    #     self.assertRaises(
    #         ValueError,
    #         Schedule70Loader.make_contract,
    #         row_wrong_schedule
    #     )
    #
    # def test_cleans_labor_category(self):
    #     row_messy_category = self.make_row(labor_category=' Messy\nCategory')
    #     contract = Schedule70Loader.make_contract(row_messy_category)
    #     self.assertEquals(contract.labor_category, 'Messy Category')
    #
    # def test_sets_hourly1_and_current_price(self):
    #     price = 999.99
    #     c = Schedule70Loader.make_contract(self.make_row(price=str(price)))
    #     self.assertEquals(c.hourly_rate_year1, price)
    #     self.assertEquals(c.current_price, price)
    #
    # def test_no_display_price_if_too_low(self):
    #     price = FEDERAL_MIN_CONTRACT_RATE - 1.0
    #     c = Schedule70Loader.make_contract(self.make_row(price=str(price)))
    #     self.assertEquals(c.hourly_rate_year1, price)
    #     self.assertIsNone(c.current_price)
