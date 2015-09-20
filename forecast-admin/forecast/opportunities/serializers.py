from rest_framework import serializers
from .models import Award

class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        exclude = ('owner',)