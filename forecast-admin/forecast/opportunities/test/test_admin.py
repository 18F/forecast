from django.test import TestCase
from django.test import Client

from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from opportunities.models import OSBUAdvisor


class OSBUAdvisorAdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.opp = OSBUAdvisor.objects.create(
            name="John Doe",
            phone="202-555-5555",
            email="john.doe@gsa.gov",
        )
        self.site = AdminSite()

    def test_default_fields(self):
        ma = ModelAdmin(OSBUAdvisor, self.site)
        self.assertEqual(
            list(ma.get_form(self.client).base_fields),
            ['name', 'email', 'phone']
        )
