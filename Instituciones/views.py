from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import Razon_social, financieras
from .serializers import FinancieraSerializer, RazonSocialSerializer

class FinancieraViews(viewsets.ModelViewSet):
    queryset = financieras.objects.all()
    serializer_class = FinancieraSerializer

class RazonSocialView(viewsets.ModelViewSet):
    queryset = Razon_social.objects.all()
    serializer_class = RazonSocialSerializer