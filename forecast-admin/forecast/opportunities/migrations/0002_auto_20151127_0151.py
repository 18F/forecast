# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year',
            field=models.IntegerField(default=2016, max_length=5),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year_quarter',
            field=models.IntegerField(default=1, max_length=200),
        ),
    ]
