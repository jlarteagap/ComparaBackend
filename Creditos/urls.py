# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import CreditoCosnumoViewSets

router = DefaultRouter()
router.register(r'api', CreditoCosnumoViewSets, basename='api')

urlpatterns = [
    path('', include(router.urls))
]