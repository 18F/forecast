from django.shortcuts import render
from .models import Opportunity, Office, OSBUAdvisor
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer
from django.core import serializers
from django.shortcuts import get_object_or_404
import json
import django_filters
import rest_framework
from .serializers import (
    OpportunitySerializer, OfficeSerializer, OSBUAdvisorSerializer
)

class PaginatedCSVRenderer (CSVRenderer):
    results_field = 'results'

    def render(self, data, media_type=None, renderer_context=None):
        if not isinstance(data, list):
            data = data.get(self.results_field, [])
        return super(PaginatedCSVRenderer, self).render(data, media_type, renderer_context)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

def home(request):
    # opportunities = Opportunity.objects.all().select_related('office__id')
    agency = Opportunity.objects.values('agency').order_by('agency').distinct('agency')
    socioeconomic = Opportunity.objects.values('socioeconomic').order_by('socioeconomic').distinct('socioeconomic')
    place_of_performance_state = Opportunity.objects.values('place_of_performance_state').order_by('place_of_performance_state').distinct('place_of_performance_state')
    naics = Opportunity.objects.values('naics').order_by('naics').distinct('naics')
    estimated_fiscal_year_quarter = Opportunity.objects.values('estimated_fiscal_year_quarter').order_by('estimated_fiscal_year_quarter').distinct('estimated_fiscal_year_quarter')
    contract_type = Opportunity.objects.values('contract_type').order_by('contract_type').distinct('contract_type')
    award_status = Opportunity.objects.values('award_status').order_by('award_status').distinct('award_status')
    return render(request, 'main.html', {
            'o': {},
            'agency': agency,
            'socioeconomic': socioeconomic,
            'place_of_performance_state': place_of_performance_state,
            'naics': naics,
            'estimated_fiscal_year_quarter': estimated_fiscal_year_quarter,
            'contract_type': contract_type,
            'award_status': award_status
        })


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
                    'estimated_fiscal_year_quarter', 'dollar_value_min', 'dollar_value_max',
                    'agency', 'contract_type', 'award_status']

class OpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    renderer_classes = (
        rest_framework.renderers.JSONRenderer,
        rest_framework.renderers.BrowsableAPIRenderer,
        PaginatedCSVRenderer,
        )
    pagination_class = LargeResultsSetPagination
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
