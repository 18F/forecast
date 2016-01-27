# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0013_auto_20160114_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='office',
            options={'ordering': ['organization']},
        ),
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name_plural': 'Procurements', 'verbose_name': 'Procurement', 'ordering': ['office']},
        ),
    ]
