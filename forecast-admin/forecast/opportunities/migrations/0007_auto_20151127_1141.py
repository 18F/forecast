# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0006_auto_20151127_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='price_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='price_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, max_length=200),
        ),
    ]
