# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opportunities.validators
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0017_auto_20160223_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='dollar_value_max',
            field=models.DecimalField(decimal_places=2, max_digits=16, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='dollar_value_min',
            field=models.DecimalField(validators=[django.core.validators.RegexValidator(message='Please enter a dollar value.', regex='\\d*(\\.\\d\\d)?')], max_digits=16, max_length=200, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='estimated_solicitation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='naics',
            field=models.CharField(verbose_name='Primary NAICS Code', validators=[opportunities.validators.validate_NAICS], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='osbu_advisor',
            field=models.ForeignKey(verbose_name='OSBU Advisor', to='opportunities.OSBUAdvisor', null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='point_of_contact_email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='point_of_contact_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
