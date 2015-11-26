from django.test import TestCase, RequestFactory
from opportunities.models import Office, Opportunity, OSBU_Advisor
from django.contrib.auth.models import User

from opportunities.serializers import OpportunitySerializer
from rest_framework.test import APITestCase

from opportunities.admin import OpportunityAdmin
from django.contrib.admin.sites import AdminSite

from opportunities.validators import validate_NAICS
from django.core.exceptions import ValidationError


class OfficeTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = Office(organization="PBS-Public Buildings Service",
                        region="R1-New England Region")

    def test_office_str(self):
        self.assertTrue(isinstance(self.o, Office))
        self.assertEqual(str(self.o),
                         "%s (%s)" % (self.o.organization, self.o.region))


class OSBU_AdvisorTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = OSBU_Advisor(name="John Doe", phone="202-555-5555",
                              email="john.doe@gsa.gov")

    def test_osbu_str(self):
        self.assertTrue(isinstance(self.o, OSBU_Advisor))
        self.assertEqual(str(self.o),
                         "%s (%s)" % (self.o.name, self.o.email))


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

    # This tests whether a 5-digit NAICS code can be saved
    def test_NAICS_validation_no_error(self):
        self.assertTrue(validate_NAICS("50105"))
