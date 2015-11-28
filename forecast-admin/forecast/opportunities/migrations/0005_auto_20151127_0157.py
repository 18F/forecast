# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0004_auto_20151127_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year_quarter',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4)], default=1),
        ),
    ]
