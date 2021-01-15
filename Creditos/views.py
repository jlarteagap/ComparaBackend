from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .models import CreditoConsumo
from .serializers import CreditoConsumoSerializer

class CreditoCosnumoViewSets(viewsets.ModelViewSet):
    serializer_class = CreditoConsumoSerializer

    queryset = CreditoConsumo.objects.all()