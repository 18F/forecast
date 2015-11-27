from rest_framework import serializers
from .models import Opportunity, Office, OSBUAdvisor


class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        # exclude = ('owner',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office


class OSBUAdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OSBUAdvisor
