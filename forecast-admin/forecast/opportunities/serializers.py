from rest_framework import serializers
from .models import Opportunity, Office


class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        exclude = ('owner',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
