from django.test import TestCase
from opportunities.models import Office, Award


class OfficeTestCase(TestCase):
    # Create your tests here.

    def setUp(self):
        self.o = Office(organization="PBS-Public Buildings Service",
                        region="R1-New England Region")

    def test_office_str(self):
        self.assertTrue(isinstance(self.o, Office))
        self.assertEqual(str(self.o),
                         "%s (%s)" % (self.o.organization, self.o.region))


class AwardTestCase(TestCase):
    def setUp(self):
        Award.objects.create(description="Test Opportunity",
                             estimated_fiscal_year="2016")

    def test_opportunity_created(self):
        award = Award.objects.get(description="Test Opportunity")
        self.assertTrue(award)

    def test_opportunity_str(self):
        award = Award.objects.get(description="Test Opportunity")
        self.assertEqual(str(award), "Test Opportunity (2016)")
