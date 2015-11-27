# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0002_auto_20151127_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year',
            field=models.IntegerField(default=2016),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year_quarter',
            field=models.IntegerField(default=1),
        ),
    ]
