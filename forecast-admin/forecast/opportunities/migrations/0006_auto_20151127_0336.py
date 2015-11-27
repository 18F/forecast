# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0005_auto_20151127_0157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OSBU_Advisor',
            new_name='OSBUAdvisor',
        ),
    ]
