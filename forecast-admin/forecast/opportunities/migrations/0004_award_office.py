# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0003_auto_20150919_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='office',
            field=models.ForeignKey(to='opportunities.Office', default=1),
        ),
    ]
