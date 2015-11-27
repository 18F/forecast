# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opportunities.validators
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_status', models.CharField(max_length=50, choices=[('Awarded', 'Awarded'), ('Award Pending', 'Award Pending'), ('Solicitation Issued', 'Solicitation Issued'), ('Drafting Solicitation', 'Drafting Solicitation'), ('Solicitation Closed', 'Solicitation Closed'), ('Planning', 'Planning'), ('Cancelled', 'Cancelled'), ('Evaluation Stage', 'Evaluation Stage'), ('Option Exercise Pending', 'Option Exercise Pending'), ('Option Exercised', 'Option Exercised')], default=0)),
                ('description', models.CharField(max_length=200, verbose_name='Product or Service Description')),
                ('place_of_performance_city', models.CharField(max_length=100, default='Washington')),
                ('place_of_performance_state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='DC')),
                ('naics', models.CharField(validators=[opportunities.validators.validate_NAICS], blank=True, max_length=5, null=True, verbose_name='Primary NAICS Code')),
                ('socioeconomic', models.CharField(max_length=50, choices=[('Small Business', 'Small Business'), ('Small Disadvantaged Business (includes Section 8a)', 'Small Disadvantaged Business (includes Section 8a)'), ('Woman-Owned Small Business', 'Woman-Owned Small Business'), ('HUBZone Small Business', 'HUBZone Small Business'), ('Service Disabled Veteran-owned Small Business', 'Service Disabled Veteran-owned Small Business'), ('Multiple Small Business Categories', 'Multiple Small Business Categories'), ('Other Than Small', 'Other Than Small'), ('AbilityOne', 'AbilityOne'), ('To Be Determined', 'To Be Determined'), ('To Be Determined-BPA', 'To Be Determined-BPA'), ('To Be Determined-IDIQ', 'To Be Determined-IDIQ')], default=8, verbose_name='Socioeconomic Category')),
                ('procurement_method', models.CharField(max_length=200, choices=[('GSA Schedule', 'GSA Schedule'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract'), ('BPA Call', 'BPA Call'), ('Purchase Order', 'Purchase Order'), ('Definitive Contract', 'Definitive Contract'), ('Ability One', 'Ability One'), ('Indefinite Delivery Indefinite Quantity-IDIQ', 'Indefinite Delivery Indefinite Quantity-IDIQ'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Contract', 'Contract'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('Indefinite Delivery Vehicle (IDV)', 'Indefinite Delivery Vehicle (IDV)'), ('Purchase Order', 'Purchase Order'), ('Order under IDV', 'Order under IDV'), ('Order under GSA Schedules Program', 'Order under GSA Schedules Program'), ('Order under GSA Schedules Program BPA', 'Order under GSA Schedules Program BPA'), ('To Be Determined', 'To Be Determined'), ('Definitive Contract other than IDV', 'Definitive Contract other than IDV'), ('Indefinite Delivery Vehicle Base Contract', 'Indefinite Delivery Vehicle Base Contract'), ('Order under GSA Federal Supply Schedules Program', 'Order under GSA Federal Supply Schedules Program'), ('Order under IDV', 'Order under IDV'), ('Purchase Order', 'Purchase Order'), ('Contract modification', 'Contract modification'), ('Ability One', 'Ability One'), ('Call Order under GSA Schedules BPA', 'Call Order under GSA Schedules BPA'), ('To Be Determined', 'To Be Determined'), ('GSA Schedule Contract', 'GSA Schedule Contract'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('BPA Call', 'BPA Call'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract')], default=20, verbose_name='Procurement Method')),
                ('contract_type', models.CharField(max_length=200, choices=[('Fixed Price with Economic Price Adjustment', 'Fixed Price with Economic Price Adjustment'), ('Fixed Price Incentive', 'Fixed Price Incentive'), ('Fixed Price Award Fee', 'Fixed Price Award Fee'), ('Cost Plus Award Fee', 'Cost Plus Award Fee'), ('Cost No Fee', 'Cost No Fee'), ('Cost Sharing', 'Cost Sharing'), ('Cost Plus Fixed Fee', 'Cost Plus Fixed Fee'), ('Cost Plus Incentive Fee', 'Cost Plus Incentive Fee'), ('Time and Materials', 'Time and Materials'), ('Labor Hours', 'Labor Hours'), ('Order Dependent', 'Order Dependent'), ('To Be Determined', 'To Be Determined'), ('Interagency Agreement', 'Interagency Agreement')], default=11, verbose_name='Contract Type')),
                ('competition_strategy', models.CharField(max_length=200, choices=[('Sole Source', 'Sole Source'), ('Full and Open', 'Full and Open'), ('Set-Aside', 'Set-Aside'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside'), ('A/E Procedures', 'A/E Procedures'), ('Full and Open Competition', 'Full and Open Competition'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Follow On to Competed Action', 'Follow On to Competed Action'), ('Competed under SAP', 'Competed under SAP'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('Competitive Delivery Order Fair Opportunity Provided', 'Competitive Delivery Order Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('Fair Opportunity', 'Fair Opportunity'), ('Sole-Source', 'Sole-Source'), ('Limited Sources', 'Limited Sources'), ('To Be Determined', 'To Be Determined'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Full and Open after exclusion of sources (competitive small business             set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Full and Open Competition Unrestricted', 'Full and Open Competition Unrestricted'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('A/E Procedures', 'A/E Procedures'), ('Competed under SAP', 'Competed under SAP'), ('Follow On to Competed Action (FAR 6.302-1)', 'Follow On to Competed Action (FAR 6.302-1)'), ('Competitive Delivery Order - Fair Opportunity Provided', 'Competitive Delivery Order - Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('To Be Determined', 'To Be Determined'), ('Limited Sources FSS Order', 'Limited Sources FSS Order'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside')], default=17)),
                ('price_min', models.DecimalField(max_digits=12, blank=True, null=True, max_length=200, decimal_places=2)),
                ('price_max', models.DecimalField(max_digits=12, blank=True, null=True, max_length=200, decimal_places=2)),
                ('delivery_order_value', models.CharField(blank=True, null=True, max_length=200)),
                ('incumbent_name', models.CharField(blank=True, null=True, max_length=200, verbose_name='Incumbent Contractor Name')),
                ('new_requirement', models.CharField(max_length=200, choices=[('New Requirement', 'New Requirement'), ('Option', 'Option'), ('To Be Determined', 'To Be Determined'), ('Recompete', 'Recompete')], default=2)),
                ('funding_agency', models.CharField(max_length=200, choices=[('GSA funded', 'GSA funded'), ('GSA funded-PBS', 'GSA funded-PBS'), ('GSA funded-FAS', 'GSA funded-FAS'), ('GSA funded-IAD', 'GSA funded-IAD'), ('GSA funded-Other', 'GSA funded-Other'), ('Non-GSA funded', 'Non-GSA funded'), ('Both', 'Both'), ('To Be Determined', 'To Be Determined')], default=7)),
                ('estimated_solicitation_date', models.DateField(blank=True, null=True)),
                ('fedbizopps_link', models.CharField(blank=True, null=True, max_length=200)),
                ('estimated_fiscal_year', models.CharField(blank=True, null=True, max_length=200)),
                ('estimated_fiscal_year_quarter', models.CharField(blank=True, null=True, max_length=200)),
                ('point_of_contact_name', models.CharField(blank=True, null=True, max_length=200)),
                ('point_of_contact_email', models.EmailField(blank=True, null=True, max_length=200)),
                ('point_of_contact_phone', localflavor.us.models.PhoneNumberField(blank=True, null=True, max_length=20)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('office', models.ForeignKey(to='opportunities.Office', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
            },
        ),
        migrations.CreateModel(
            name='OSBU_Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, max_length=200)),
                ('email', models.EmailField(blank=True, null=True, max_length=200)),
                ('phone', localflavor.us.models.PhoneNumberField(blank=True, null=True, max_length=20)),
            ],
            options={
                'verbose_name': 'OSBU Advisor',
            },
        ),
        migrations.AddField(
            model_name='opportunity',
            name='osbu_advisor',
            field=models.ForeignKey(to='opportunities.OSBU_Advisor', blank=True, null=True),
        ),
    ]
