# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0012_auto_20160106_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_fiscal_year_quarter',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('To Be Determined', 'To Be Determined')], default='To Be Determined', max_length=50),
        ),
    ]
