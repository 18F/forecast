# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0008_auto_20151208_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'Procurements', 'verbose_name': 'Procurement'},
        ),
    ]
