from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'crime', views.CrimeViewSet)
router.register(r'warrant', views.WarrantViewSet)
router.register(r'citizen', views.CitizenViewSet)
router.register(r'license_plate', views.LicensePlateViewSet)
router.register(r'officer', views.OfficerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]