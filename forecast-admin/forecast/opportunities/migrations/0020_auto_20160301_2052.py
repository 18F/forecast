# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0019_auto_20160225_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='agency',
            field=models.CharField(max_length=100, default='GSA', editable=False),
        ),
        migrations.AlterField(
            model_name='office',
            name='region',
            field=models.CharField(max_length=100, choices=[('Region 1', 'Region 1'), ('Region 2', 'Region 2'), ('Region 3', 'Region 3'), ('Region 4', 'Region 4'), ('Region 5', 'Region 5'), ('Region 6', 'Region 6'), ('Region 7', 'Region 7'), ('Region 8', 'Region 8'), ('Region 9', 'Region 9'), ('Region 10', 'Region 10'), ('National Capital Region', 'National Capital Region'), ('Central Office', 'Central Office')]),
        ),
    ]
