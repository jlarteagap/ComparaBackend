# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import RazonSocialView, FinancieraViews

router = DefaultRouter()
router.register(r'financieras', FinancieraViews, basename='Financieras')
router.register(r'razon_social', RazonSocialView, basename='Razon Social')

urlpatterns = [
    path('', include(router.urls))
]