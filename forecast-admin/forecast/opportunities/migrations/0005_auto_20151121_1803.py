# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0004_award_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='competition_strategy',
            field=models.CharField(null=True, blank=True, choices=[('Sole Source', 'Sole Source'), ('Full and Open', 'Full and Open'), ('Set-Aside', 'Set-Aside'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside'), ('A/E Procedures', 'A/E Procedures'), ('Full and Open Competition', 'Full and Open Competition'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Follow On to Competed Action', 'Follow On to Competed Action'), ('Competed under SAP', 'Competed under SAP'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('Competitive Delivery Order Fair Opportunity Provided', 'Competitive Delivery Order Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('Fair Opportunity', 'Fair Opportunity'), ('Sole-Source', 'Sole-Source'), ('Limited Sources', 'Limited Sources'), ('To Be Determined', 'To Be Determined'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Full and Open after exclusion of sources (competitive small business             set-asides, competitive 8a)', 'Full and Open after exclusion of sources (competitive small             business set-asides, competitive 8a)'), ('Full and Open Competition Unrestricted', 'Full and Open Competition Unrestricted'), ('Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)', 'Not Available for Competition (e.g., 8a sole source, HUBZone &             SDVOSB sole source, Ability One, all > SAT)'), ('Not Competed (e.g., sole source, urgency, etc., all > SAT)', 'Not Competed (e.g., sole source, urgency, etc., all > SAT)'), ('Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)', 'Not Competed under SAP (e.g., Urgent, Sole source, Logical             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)'), ('A/E Procedures', 'A/E Procedures'), ('Competed under SAP', 'Competed under SAP'), ('Follow On to Competed Action (FAR 6.302-1)', 'Follow On to Competed Action (FAR 6.302-1)'), ('Competitive Delivery Order - Fair Opportunity Provided', 'Competitive Delivery Order - Fair Opportunity Provided'), ('Non-Competitive Delivery Order', 'Non-Competitive Delivery Order'), ('To Be Determined', 'To Be Determined'), ('Limited Sources FSS Order', 'Limited Sources FSS Order'), ('Competitive Schedule Buy', 'Competitive Schedule Buy'), ('Partial Small Business Set-Aside', 'Partial Small Business Set-Aside')], max_length=200),
        ),
    ]
