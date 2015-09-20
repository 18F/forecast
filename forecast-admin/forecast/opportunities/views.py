from django.shortcuts import render
from .models import Award
from rest_framework import viewsets
from .serializers import AwardSerializer

class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
