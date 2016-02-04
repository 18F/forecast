# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0009_auto_20160105_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opportunity',
            old_name='price_max',
            new_name='dollar_value_max',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='price_min',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='dollar_value_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=16, validators=[django.core.validators.RegexValidator(regex='\\d*(\\.\\d\\d)?', message='Please enter a dollar value.')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='including_options',
            field=models.BooleanField(default=False),
        ),
    ]
