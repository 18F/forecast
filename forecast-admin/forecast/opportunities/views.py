from django.shortcuts import render
from .models import Opportunity, Office, OSBUAdvisor
from rest_framework import viewsets, filters
from django.core import serializers
from django.shortcuts import get_object_or_404
import json
import django_filters
from .serializers import (
    OpportunitySerializer, OfficeSerializer, OSBUAdvisorSerializer
)

def home(request):
    opportunities = Opportunity.objects.all().select_related('office__id')
    return render(request, 'main.html', {'o': opportunities})


def details(request, id):
    """
    A page displaying details about a particular contracting opportunity
    """
    opportunity = get_object_or_404(Opportunity.objects.filter(id=id).select_related('office__id', 'osbu_advisor__id'))
    return render(request, 'detail.html', {'o': opportunity})

class OpportunityFilter(django_filters.FilterSet):
    """
    Filters available when calling the API endpoint
    """
    description = django_filters.CharFilter(lookup_type='icontains')
    dollar_value_min = django_filters.NumberFilter(lookup_type='gt')
    dollar_value_max = django_filters.NumberFilter(lookup_type='lt')
    class Meta:
        model = Opportunity
        fields = ['socioeconomic','place_of_performance_state','naics','description',
                    'estimated_fiscal_year_quarter', 'dollar_value_min', 'dollar_value_max']

class OpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Opportunity.objects.all().filter(published=True)
    serializer_class = OpportunitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = OpportunityFilter


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
