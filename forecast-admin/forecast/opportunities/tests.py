from django.test import TestCase, RequestFactory
from opportunities.models import Office, Opportunity
from django.contrib.auth.models import User

from opportunities.serializers import OpportunitySerializer
from rest_framework.test import APITestCase

from opportunities.admin import OpportunityAdmin
from django.contrib.admin.sites import AdminSite


class OfficeTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = Office(organization="PBS-Public Buildings Service",
                        region="R1-New England Region")

    def test_office_str(self):
        self.assertTrue(isinstance(self.o, Office))
        self.assertEqual(str(self.o),
                         "%s (%s)" % (self.o.organization, self.o.region))


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
