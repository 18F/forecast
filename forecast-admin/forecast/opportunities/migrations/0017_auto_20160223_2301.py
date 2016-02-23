# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0016_auto_20160223_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Product or Service Description'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='incumbent_name',
            field=models.CharField(max_length=400, null=True, verbose_name='Incumbent Contractor Name', blank=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='socioeconomic',
            field=models.CharField(default='To Be Determined', choices=[('Small Business', 'Small Business'), ('Small Disadvantaged Business (includes Section 8a)', 'Small Disadvantaged Business (includes Section 8a)'), ('Woman-Owned Small Business', 'Woman-Owned Small Business'), ('HUBZone Small Business', 'HUBZone Small Business'), ('Service Disabled Veteran-owned Small Business', 'Service Disabled Veteran-owned Small Business'), ('Multiple Small Business Categories', 'Multiple Small Business Categories'), ('Other Than Small', 'Other Than Small'), ('AbilityOne', 'AbilityOne'), ('To Be Determined', 'To Be Determined'), ('To Be Determined-BPA', 'To Be Determined-BPA'), ('To Be Determined-IDIQ', 'To Be Determined-IDIQ')], verbose_name='Socioeconomic Category', max_length=100),
        ),
    ]
