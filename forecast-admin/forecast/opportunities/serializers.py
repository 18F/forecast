from rest_framework import serializers
from .models import Opportunity, Office, OSBUAdvisor


class OpportunitySerializer(serializers.ModelSerializer):
    office = serializers.ReadOnlyField(source='office.organization')

    class Meta:
        model = Opportunity
        # exclude = ('owner',)


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office


class OSBUAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSBUAdvisor
