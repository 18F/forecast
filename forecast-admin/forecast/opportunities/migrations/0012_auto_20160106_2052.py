# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_auto_20160105_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='osbu_advisor',
            field=models.ForeignKey(verbose_name='OSBU Advisor', null=True, to='opportunities.OSBUAdvisor', blank=True),
        ),
    ]
