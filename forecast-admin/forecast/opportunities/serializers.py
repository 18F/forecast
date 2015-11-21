from rest_framework import serializers
from .models import Award, Office


class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        exclude = ('owner',)


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Office
