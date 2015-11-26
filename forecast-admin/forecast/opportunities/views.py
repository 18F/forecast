from django.shortcuts import render
from .models import Opportunity, Office
from rest_framework import viewsets
from .serializers import OpportunitySerializer, OfficeSerializer, OSBU_Advisor


def home(request):
    return render(request, 'main.html')


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


class OSBU_AdvisorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OSBU_Advisor.objects.all()
    serializer_class = OSBU_Advisor
