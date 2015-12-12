# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opportunities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0007_auto_20151127_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='naics',
            field=models.CharField(null=True, blank=True, max_length=6, verbose_name='Primary NAICS Code', validators=[opportunities.validators.validate_NAICS]),
        ),
    ]
