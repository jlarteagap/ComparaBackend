from django.contrib import admin

# Register your models here.
from creditoHipotecarios.models import CreditoHipotecario, ImpuestoTRe

admin.site.register(CreditoHipotecario);
admin.site.register(ImpuestoTRe);