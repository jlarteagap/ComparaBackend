from django.db import models

# Create your models here.
class InstitucionesFinancieras(models.Model):

    name = models.CharField(max_length=50)
    logo = models.ImageField(null = True, blank = True)

    class Meta:
        verbose_name = ("Instituciones Financiera")
        verbose_name_plural = ("InstitucionesFinancieras")

    def __str__(self):
        return self.name

