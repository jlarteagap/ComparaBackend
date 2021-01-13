from django.db import models

# Create your models here.
class Razon_social(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Razon social")
        verbose_name_plural = ("Razon social")

    def __str__(self):
        return self.name


class financieras(models.Model):

    name = models.CharField( max_length=250)
    razon_social = models.ForeignKey(Razon_social, on_delete=models.CASCADE, null = True)
    logo = models.ImageField(null = True, blank = True)

    class Meta:
        verbose_name = ("Entidad Financiera")
        verbose_name_plural = ("Entidades Financieras")

    def __str__(self):
        return self.name
