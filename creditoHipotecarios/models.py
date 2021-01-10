from django.db import models

# Create your models here.
class CreditoHipotecario(models.Model):

    Banco = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("CreditoHipotecario")
        verbose_name_plural = ("CreditoHipotecarios")

    def __str__(self):
        return self.name
