# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0005_auto_20151121_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award_status',
            field=models.CharField(choices=[('Awarded', 'Awarded'), ('Award Pending', 'Award Pending'), ('Solicitation Issued', 'Solicitation Issued'), ('Drafting Solicitation', 'Drafting Solicitation'), ('Solicitation Closed', 'Solicitation Closed'), ('Planning', 'Planning'), ('Cancelled', 'Cancelled'), ('Evaluation Stage', 'Evaluation Stage'), ('Option Exercise Pending', 'Option Exercise Pending'), ('Option Exercised', 'Option Exercised')], max_length=50, default='Planning'),
        ),
    ]
