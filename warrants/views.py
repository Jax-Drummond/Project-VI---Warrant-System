import rest_framework.permissions
from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializer import *

# Create your views here.
class WarrantViewSet(viewsets.ModelViewSet):
    queryset = Warrant.objects.all()
    serializer_class = WarrantSerializer

class CrimeViewSet(viewsets.ModelViewSet):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class LicensePlateViewSet(viewsets.ModelViewSet):
    queryset = License_Plate.objects.all()
    serializer_class = License_PlateSerializer

class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer



## Frontend Views
@login_required
def dashboard_view(request):
    return render(request, 'warrants/dashboard.html')