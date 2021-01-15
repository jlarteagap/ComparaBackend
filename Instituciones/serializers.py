from rest_framework import serializers
from .models import financieras, Razon_social

class RazonSocialSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Razon_social
        fields = "__all__"

class FinancieraSerializer(serializers.ModelSerializer):

    razon_social = RazonSocialSerializer(read_only = True)

    class Meta:
        model = financieras
        fields = "__all__"