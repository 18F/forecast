# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_status', models.CharField(choices=[('Pending', 'Award Pending'), ('Awarded', 'Awarded')], max_length=50)),
                ('description', models.CharField(max_length=200, null=True, blank=True, verbose_name='Product or Service Description')),
                ('place_of_performance_city', models.CharField(max_length=100, default='Washington')),
                ('place_of_performance_state', localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2, default='DC')),
                ('naics', models.CharField(max_length=20, null=True, blank=True, verbose_name='Primary NAICS Code')),
                ('socioeconomic', models.CharField(max_length=50, null=True, blank=True, verbose_name='Socioeconomic Category')),
                ('procurement_method', models.CharField(max_length=200, null=True, blank=True, verbose_name='Procurement Method')),
                ('competition_strategy', models.CharField(max_length=200, null=True, blank=True)),
                ('price_min', models.CharField(max_length=200, null=True, blank=True)),
                ('price_max', models.CharField(max_length=200, null=True, blank=True)),
                ('delivery_order_value', models.CharField(max_length=200, null=True, blank=True)),
                ('incumbent_name', models.CharField(max_length=200, null=True, blank=True, verbose_name='Incumbent Contractor Name')),
                ('new_requirement', models.CharField(max_length=200, null=True, blank=True)),
                ('funding_agency', models.CharField(max_length=200, null=True, blank=True)),
                ('estimated_solicitation_date', models.DateField(null=True, blank=True)),
                ('fedbizopps_link', models.CharField(max_length=200, null=True, blank=True)),
                ('estimated_fiscal_year', models.CharField(max_length=200, null=True, blank=True)),
                ('estimated_fiscal_year_quarter', models.CharField(max_length=200, null=True, blank=True)),
                ('point_of_contact_name', models.CharField(max_length=200, null=True, blank=True)),
                ('point_of_contact_email', models.EmailField(max_length=200, null=True, blank=True)),
                ('point_of_contact_phone', localflavor.us.models.PhoneNumberField(max_length=20, null=True, blank=True)),
                ('osbu_advisor_name', models.CharField(max_length=200, null=True, blank=True)),
                ('osbu_advisor_email', models.EmailField(max_length=200, null=True, blank=True)),
                ('osbu_advisor_phone', localflavor.us.models.PhoneNumberField(max_length=20, null=True, blank=True)),
                ('additional_information', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
            ],
        ),
    ]
