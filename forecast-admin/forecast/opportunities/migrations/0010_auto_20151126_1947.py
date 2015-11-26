# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0009_auto_20151126_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSBU_Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('osbu_advisor_name', models.CharField(null=True, blank=True, max_length=200)),
                ('osbu_advisor_email', models.EmailField(null=True, blank=True, max_length=200)),
                ('osbu_advisor_phone', localflavor.us.models.PhoneNumberField(null=True, blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='osbu_advisor_email',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='osbu_advisor_name',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='osbu_advisor_phone',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='osbu_advisor',
            field=models.ForeignKey(to='opportunities.OSBU_Advisor', null=True, blank=True),
        ),
    ]
