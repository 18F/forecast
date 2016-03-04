import os, csv
from datetime import date

from django.test import TestCase, RequestFactory
from opportunities.models import Office, Opportunity, OSBUAdvisor
from django.contrib.auth.models import User

from opportunities.serializers import OpportunitySerializer
from rest_framework.test import APITestCase

from opportunities.admin import OpportunityAdmin
from django.contrib.admin.sites import AdminSite

from opportunities.validators import validate_NAICS
from django.core.exceptions import ValidationError

from django.core.management import call_command
from opportunities.management.commands.load_opportunities import OpportunitiesLoader

from django.template import Context, Template

class OfficeTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = Office(organization="PBS-Public Buildings Service",
                        region="R1-New England Region")

    def test_office_str(self):
        self.assertTrue(isinstance(self.o, Office))
        self.assertEqual(str(self.o),
                         "%s (%s)" % (self.o.organization, self.o.region))


class OSBUAdvisorTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = OSBUAdvisor(name="John Doe", phone="202-555-5555",
                             email="john.doe@gsa.gov")

    def test_osbu_str(self):
        self.assertTrue(isinstance(self.o, OSBUAdvisor))
        self.assertEqual(str(self.o),
                         "%s (%s, %s)" % (self.o.name, self.o.email, self.o.phone))


class OpportunityTestCase(TestCase):
    def setUp(self):
        Opportunity.objects.create(description="Test Opportunity",
                                   estimated_fiscal_year="2016")

    def test_opportunity_created(self):
        award = Opportunity.objects.get(description="Test Opportunity")
        self.assertTrue(award)

    def test_opportunity_str(self):
        award = Opportunity.objects.get(description="Test Opportunity")
        self.assertEqual(str(award), "Test Opportunity (2016)")

    def test_opportunity_NAICS_error(self):
        o = Opportunity.objects.create(naics="2016")
        self.assertRaises(ValidationError, o.save())


# Testing the Award API
class OpportunityAPITest(APITestCase):
    def setUp(self):
        self.o = Office(organization="PBS-Public Buildings Service",
                        region="R1-New England Region")
        self.a = Opportunity(office=self.o, description="Test Opportunity",
                             estimated_fiscal_year="2016")

    def test_API(self):
        response = self.client.get('/api/opportunities/')
        self.assertEqual(200, response.status_code)


class ValidatorsTestCase(TestCase):
    # This tests whether a 4-digit NAICS code raises a Validation Error
    # Passing the test means that the 4-digit data results in error.
    def test_NAICS_validation(self):
        with self.assertRaises(ValidationError):
            validate_NAICS("5010")

    # This tests ensures that only digits can be used, else Validation Error
    # Passing the test means that the a non-digit results in error.
    def test_NAICS_validation(self):
        with self.assertRaises(ValidationError):
            validate_NAICS("1010a")

    # This tests whether a 6-digit NAICS code can be saved
    def test_NAICS_validation_no_error(self):
        self.assertTrue(validate_NAICS("501056"))

class ImporterTestCase(TestCase):
    sample_filename = 'test/data/sample.csv'
    bad_filename = 'test/data/bad_sample.csv'

    def load(self, filename, **kwargs):
        call_command(
            'load_opportunities',
            filename=os.path.join(os.path.dirname(__file__), filename)
        )

    def test_loads_sample(self):
        filename = os.path.join(os.path.dirname(__file__), self.sample_filename)
        self.load(self.sample_filename)
        with open(filename) as f:
            has_header = csv.Sniffer().has_header(f.read(1024))
            file_read = csv.reader(f)
            rows = sum(1 for row in file_read)
        self.assertEquals(Opportunity.objects.count(), rows)

    def test_parse_date(self):
        parse_date = OpportunitiesLoader.parse_date
        self.assertEquals(parse_date('12/8/2015'), date(2015, 12, 8))
        self.assertEquals(parse_date('06/03/2014'), date(2014, 6, 3))
        self.assertEquals(parse_date('5/1/2016'), date(2016, 5, 1))
        self.assertIsNone(parse_date(''))

    def test_parse_fiscal_dates(self):
        parse_fiscal_dates = OpportunitiesLoader.parse_fiscal_dates
        self.assertEquals(parse_fiscal_dates("FY 2016-2nd Quarter"),("2016","2nd"))
        self.assertEquals(parse_fiscal_dates("FY 2016-Quarter To Be Determined"),
                                                ("2016","To Be Determined"))
        self.assertEquals(parse_fiscal_dates("FY 2016-Quarter 4"), ("2016","4th"))

    def test_parse_dollars(self):
        parse_dollars = OpportunitiesLoader.parse_dollars
        self.assertEquals(parse_dollars('$1000'), 1000)
        self.assertEquals(parse_dollars('$5,000'), 5000)
        self.assertIsNone(parse_dollars(1000))

    def test_parse_advisor(self):
        parse_advisor = OpportunitiesLoader.parse_advisor
        self.assertEquals(parse_advisor('Really Fakeperson, 555-555-5555, really.fakeperson@gsa.gov'),
            ['Really Fakeperson', '555-555-5555', 'really.fakeperson@gsa.gov'])
        self.assertEquals(parse_advisor('Different Fakeperson, 555-555-5555 different.fakeperson@gsa.gov'),
            ['Different Fakeperson', '555-555-5555', 'different.fakeperson@gsa.gov'])
        self.assertIsNone(parse_advisor('TBD'))

class CutTests(TestCase):

    TEMPLATE = Template("{% load filters %} {{ '123-456-7890'|cut:'-' }}")

    def setUp(self):
        self.entry = '1234567890'

    def test_cut(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(self.entry, rendered)

class CurrencyTests(TestCase):

    TEMPLATE = Template("{% load filters %} {{ '1234.56'|currency:'-' }}")

    def setUp(self):
        self.entry = '$1,234.56'

    def test_currency(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(self.entry, rendered)
