# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0021_auto_20160302_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='socioeconomic',
            field=models.CharField(default='To Be Determined', verbose_name='Socioeconomic Category', choices=[('Small Business', 'Small Business'), ('Small Disadvantaged Business (includes Section 8a)', 'Small Disadvantaged Business (includes Section 8a)'), ('Woman-Owned Small Business', 'Woman-Owned Small Business'), ('HUBZone Small Business', 'HUBZone Small Business'), ('Service Disabled Veteran-owned Small Business', 'Service Disabled Veteran-owned Small Business'), ('Veteran-owned Small Business,', 'Veteran-owned Small Business'), ('Multiple Small Business Categories', 'Multiple Small Business Categories'), ('Other Than Small', 'Other Than Small'), ('AbilityOne', 'AbilityOne'), ('To Be Determined', 'To Be Determined'), ('To Be Determined-BPA', 'To Be Determined-BPA'), ('To Be Determined-IDIQ', 'To Be Determined-IDIQ')], max_length=100),
        ),
    ]
