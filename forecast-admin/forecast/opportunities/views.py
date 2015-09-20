from django.shortcuts import render
from .models import Award, Office
from rest_framework import viewsets
from .serializers import AwardSerializer, OfficeSerializer

class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
