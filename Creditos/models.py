from django.db import models

# from Instituciones.models import EntidadesFinancieras
from Instituciones.models import financieras
# Create your models here.
class CreditoConsumo(models.Model):

    name = models.CharField( max_length=50 )
    interes = models.DecimalField(max_digits=5, decimal_places=2)
    institucion = models.ForeignKey('Instituciones.financieras', on_delete=models.CASCADE, blank = False, null = True)

    class Meta:
        verbose_name = ("Credito Consumo")
        verbose_name_plural = ("Credito Consumos")

    def __str__(self):
        return self.name

class Hipetcario(models.Model):

    name = models.CharField(("Nombre"), max_length=50)
    interes = models.DecimalField( max_digits=5, decimal_places=2, null = True)

    class Meta:
        verbose_name = ("Hipetcario")
        verbose_name_plural = ("Hipetcarios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Hipetcario_detail", kwargs={"pk": self.pk})
