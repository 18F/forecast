from rest_framework import serializers
from .models import Opportunity, Office, OSBUAdvisor

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('organization', 'region')
        

class OpportunitySerializer(serializers.ModelSerializer):
    # office = serializers.ReadOnlyField(source='office.organization')
    office = OfficeSerializer()

    class Meta:
        model = Opportunity
        # exclude = ('owner',)


class OSBUAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSBUAdvisor
