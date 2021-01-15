from rest_framework import serializers
from Creditos.models import CreditoConsumo

from Instituciones.serializers import FinancieraSerializer

class CreditoConsumoSerializer(serializers.ModelSerializer):

    institucion = FinancieraSerializer(read_only = True)

    class Meta:
        model = CreditoConsumo
        fields = ('name', 'interes', 'institucion')