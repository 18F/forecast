# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0014_auto_20160120_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='organization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='office',
            name='region',
            field=models.CharField(max_length=100),
        ),
    ]
