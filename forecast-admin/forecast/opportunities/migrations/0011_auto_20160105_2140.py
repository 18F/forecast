# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0010_auto_20160105_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2016),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year_quarter',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4)], choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('TBD', 'TBD')], default=1),
        ),
    ]
