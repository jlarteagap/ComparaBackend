from django.db import models
from Instituciones.models import InstitucionesFinancieras
# Create your models here.
class CreditoHipotecario(models.Model):
    # name = models.ForeignKey("InstitucionesFinancieras",ßon_delete=models.CASCADE)
    name = models.CharField( max_length=50, null = True)
    Interes = models.DecimalField(max_digits=2, decimal_places=2, null = True)
    # Interes = models.IntegerField(null = True)

    class Meta:
        verbose_name = ("Credito Hipotecario")
        verbose_name_plural = ("Credito Hipotecarios")

    def __str__(self):
        return self.name

class ImpuestoTRe(models.Model):
    TreMN = models.DecimalField(null = True, max_digits=5, decimal_places=2)
    TReMD = models.DecimalField(null = True, max_digits=5, decimal_places=2)
    TReUFV = models.DecimalField(null = True,max_digits=5, decimal_places=2)
    TReME = models.DecimalField(null = True, max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = ("Impuesto TRe")
        verbose_name_plural = ("Impuesto TRes")

    def __str__(self):
        return "Impuesto 2021"
