from django.shortcuts import render
from .models import Opportunity, Office
from rest_framework import viewsets
from .serializers import OpportunitySerializer, OfficeSerializer


class OpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Opportunity.objects.all().filter(published=True)
    serializer_class = OpportunitySerializer


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
