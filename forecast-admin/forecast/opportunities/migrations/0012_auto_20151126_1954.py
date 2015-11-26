# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_auto_20151126_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'Opportunities'},
        ),
        migrations.AlterModelOptions(
            name='osbu_advisor',
            options={'verbose_name': 'OSBU Advisor'},
        ),
    ]
