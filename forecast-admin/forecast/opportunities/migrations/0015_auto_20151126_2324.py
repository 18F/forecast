# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opportunities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0014_auto_20151126_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='price_max',
            field=models.DecimalField(null=True, blank=True, validators=[opportunities.validators.validate_dollars], max_length=200, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='price_min',
            field=models.DecimalField(null=True, blank=True, validators=[opportunities.validators.validate_dollars], max_length=200, max_digits=12, decimal_places=2),
        ),
    ]
