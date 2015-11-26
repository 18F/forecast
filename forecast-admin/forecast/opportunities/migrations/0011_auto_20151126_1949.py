# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0010_auto_20151126_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osbu_advisor',
            old_name='osbu_advisor_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='osbu_advisor',
            old_name='osbu_advisor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='osbu_advisor',
            old_name='osbu_advisor_phone',
            new_name='phone',
        ),
    ]
