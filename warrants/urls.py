from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

router = routers.DefaultRouter()

router.register(r'crime', views.CrimeViewSet)
router.register(r'warrant', views.WarrantViewSet, basename='warrant')
router.register(r'citizen', views.CitizenViewSet)
router.register(r'license_plate', views.LicensePlateViewSet)
router.register(r'officer', views.OfficerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]