# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0013_auto_20151126_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='award_status',
            field=models.CharField(choices=[('Awarded', 'Awarded'), ('Award Pending', 'Award Pending'), ('Solicitation Issued', 'Solicitation Issued'), ('Drafting Solicitation', 'Drafting Solicitation'), ('Solicitation Closed', 'Solicitation Closed'), ('Planning', 'Planning'), ('Cancelled', 'Cancelled'), ('Evaluation Stage', 'Evaluation Stage'), ('Option Exercise Pending', 'Option Exercise Pending'), ('Option Exercised', 'Option Exercised')], max_length=50, default=0),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='competition_strategy',
            field=models.CharField(choices=[('Sole Source', 'Sole Source'), ('Full and Open', 'Full and Open'), ('Set-Aside', 'Set-Aside'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside'), ('A/E Procedures', 'A/E Procedures'), ('Full and Open Competition', 'Full and Open Competition'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Follow On to Competed Action', 'Follow On to Competed Action'), ('Competed under SAP', 'Competed under SAP'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('Competitive Delivery Order Fair Opportunity Provided', 'Competitive Delivery Order Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('Fair Opportunity', 'Fair Opportunity'), ('Sole-Source', 'Sole-Source'), ('Limited Sources', 'Limited Sources'), ('To Be Determined', 'To Be Determined'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Full and Open after exclusion of sources (competitive small business             set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Full and Open Competition Unrestricted', 'Full and Open Competition Unrestricted'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('A/E Procedures', 'A/E Procedures'), ('Competed under SAP', 'Competed under SAP'), ('Follow On to Competed Action (FAR 6.302-1)', 'Follow On to Competed Action (FAR 6.302-1)'), ('Competitive Delivery Order - Fair Opportunity Provided', 'Competitive Delivery Order - Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('To Be Determined', 'To Be Determined'), ('Limited Sources FSS Order', 'Limited Sources FSS Order'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside')], max_length=200, default=17),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='contract_type',
            field=models.CharField(choices=[('Fixed Price with Economic Price Adjustment', 'Fixed Price with Economic Price Adjustment'), ('Fixed Price Incentive', 'Fixed Price Incentive'), ('Fixed Price Award Fee', 'Fixed Price Award Fee'), ('Cost Plus Award Fee', 'Cost Plus Award Fee'), ('Cost No Fee', 'Cost No Fee'), ('Cost Sharing', 'Cost Sharing'), ('Cost Plus Fixed Fee', 'Cost Plus Fixed Fee'), ('Cost Plus Incentive Fee', 'Cost Plus Incentive Fee'), ('Time and Materials', 'Time and Materials'), ('Labor Hours', 'Labor Hours'), ('Order Dependent', 'Order Dependent'), ('To Be Determined', 'To Be Determined'), ('Interagency Agreement', 'Interagency Agreement')], max_length=200, verbose_name='Contract Type', default=11),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='funding_agency',
            field=models.CharField(choices=[('GSA funded', 'GSA funded'), ('GSA funded-PBS', 'GSA funded-PBS'), ('GSA funded-FAS', 'GSA funded-FAS'), ('GSA funded-IAD', 'GSA funded-IAD'), ('GSA funded-Other', 'GSA funded-Other'), ('Non-GSA funded', 'Non-GSA funded'), ('Both', 'Both'), ('To Be Determined', 'To Be Determined')], max_length=200, default=7),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='new_requirement',
            field=models.CharField(choices=[('New Requirement', 'New Requirement'), ('Option', 'Option'), ('To Be Determined', 'To Be Determined'), ('Recompete', 'Recompete')], max_length=200, default=2),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='procurement_method',
            field=models.CharField(choices=[('GSA Schedule', 'GSA Schedule'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract'), ('BPA Call', 'BPA Call'), ('Purchase Order', 'Purchase Order'), ('Definitive Contract', 'Definitive Contract'), ('Ability One', 'Ability One'), ('Indefinite Delivery Indefinite Quantity-IDIQ', 'Indefinite Delivery Indefinite Quantity-IDIQ'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Contract', 'Contract'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('Indefinite Delivery Vehicle (IDV)', 'Indefinite Delivery Vehicle (IDV)'), ('Purchase Order', 'Purchase Order'), ('Order under IDV', 'Order under IDV'), ('Order under GSA Schedules Program', 'Order under GSA Schedules Program'), ('Order under GSA Schedules Program BPA', 'Order under GSA Schedules Program BPA'), ('To Be Determined', 'To Be Determined'), ('Definitive Contract other than IDV', 'Definitive Contract other than IDV'), ('Indefinite Delivery Vehicle Base Contract', 'Indefinite Delivery Vehicle Base Contract'), ('Order under GSA Federal Supply Schedules Program', 'Order under GSA Federal Supply Schedules Program'), ('Order under IDV', 'Order under IDV'), ('Purchase Order', 'Purchase Order'), ('Contract modification', 'Contract modification'), ('Ability One', 'Ability One'), ('Call Order under GSA Schedules BPA', 'Call Order under GSA Schedules BPA'), ('To Be Determined', 'To Be Determined'), ('GSA Schedule Contract', 'GSA Schedule Contract'), ('Negotiated', 'Negotiated'), ('Sealed Bid', 'Sealed Bid'), ('Government-wide Agency Contract-GWAC', 'Government-wide Agency Contract-GWAC'), ('Commercial Item Contract', 'Commercial Item Contract'), ('GSA Schedules Program BPA', 'GSA Schedules Program BPA'), ('BPA Call', 'BPA Call'), ('Basic Ordering Agreement', 'Basic Ordering Agreement'), ('Blanket Purchase Agreement-BPA', 'Blanket Purchase Agreement-BPA'), ('Multi-Agency Contract', 'Multi-Agency Contract')], max_length=200, verbose_name='Procurement Method', default=20),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='socioeconomic',
            field=models.CharField(choices=[('Small Business', 'Small Business'), ('Small Disadvantaged Business (includes Section 8a)', 'Small Disadvantaged Business (includes Section 8a)'), ('Woman-Owned Small Business', 'Woman-Owned Small Business'), ('HUBZone Small Business', 'HUBZone Small Business'), ('Service Disabled Veteran-owned Small Business', 'Service Disabled Veteran-owned Small Business'), ('Multiple Small Business Categories', 'Multiple Small Business Categories'), ('Other Than Small', 'Other Than Small'), ('AbilityOne', 'AbilityOne'), ('To Be Determined', 'To Be Determined'), ('To Be Determined-BPA', 'To Be Determined-BPA'), ('To Be Determined-IDIQ', 'To Be Determined-IDIQ')], max_length=50, verbose_name='Socioeconomic Category', default=8),
        ),
    ]
