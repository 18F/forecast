from django.shortcuts import render
from .models import Opportunity, Office, OSBUAdvisor
from rest_framework import viewsets
from django.core import serializers
import json
from .serializers import (
    OpportunitySerializer, OfficeSerializer, OSBUAdvisorSerializer
)


def home(request):
    opportunities = serializers.serialize("json", Opportunity.objects.all(),
                                            use_natural_foreign_keys=True,
                                            use_natural_primary_keys=True)
    opportunities = json.loads(opportunities)
    return render(request, 'main.html', {'o': opportunities})


def details(request, id):
    """
    A page displaying details about a particular contracting opportunity
    """
    opportunity = serializers.serialize("json", Opportunity.objects.all().filter(id=id),
                                            use_natural_foreign_keys=True,
                                            use_natural_primary_keys=True)
    opportunity = json.loads(opportunity)
    return render(request, 'detail.html', {'o': opportunity[0]["fields"]})


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


class OSBUAdvisorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OSBUAdvisor.objects.all()
    serializer_class = OSBUAdvisorSerializer
