from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create User '

    def handle(self, *args, **options):
        g, created = Group.objects.get_or_create(name='GSA_staff')
        opp_add_perm = Permission.objects.get(name='Can add opportunity')
        opp_change_perm = Permission.objects.get(name='Can change opportunity')
        g.permissions.add(opp_add_perm)
        g.permissions.add(opp_change_perm)
