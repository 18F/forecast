from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User, Group, Permission

from django.core.management import call_command
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


class OfficeAuthorizationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testUserNoPerm")
        self.user.is_staff = True
        self.user.save()

    def test_command_output(self):
        """
        Test management command to see if GSA_staff group is created with
        permission to add and change opportunities.
        """
        call_command('create_GSA_staff_group')
        g, created = Group.objects.get_or_create(name='GSA_staff')
        opp_add_perm = Permission.objects.get(name='Can add opportunity')
        opp_change_perm = Permission.objects.get(name='Can change opportunity')
        self.assertEqual(g.permissions.filter(
            name='Can add opportunity')[0],
            opp_add_perm
        )
        self.assertEqual(g.permissions.filter(
            name='Can change opportunity')[0],
            opp_change_perm
        )
