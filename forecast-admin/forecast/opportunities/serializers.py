from rest_framework import serializers
from .models import Opportunity, Office, OSBU_Advisor


class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        # exclude = ('owner',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office


class OSBU_AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OSBU_Advisor
