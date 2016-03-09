# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0020_auto_20160301_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Product or Service Description'),
        ),
    ]
