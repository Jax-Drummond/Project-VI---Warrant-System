from django.shortcuts import render
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import *
from .serializer import *

# Create your views here.
class WarrantViewSet(viewsets.ModelViewSet):
    serializer_class = WarrantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Warrant.objects.all()

        # Get the 'search' param from the URL (e.g., ?search=Jones)
        query = self.request.query_params.get('search', None)

        if query:
            queryset = queryset.filter(
                Q(citizen_involved__first_name__icontains=query) |
                Q(citizen_involved__last_name__icontains=query) |
                Q(citizen_involved__plates__plate_number__icontains=query) |
                Q(crime_number__description__icontains=query)
            ).distinct()

        return queryset

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
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

## Frontend Views
@login_required
def dashboard_view(request):
    return render(request, 'warrants/dashboard.html')

@login_required
def warrants_view(request):
    return render(request, 'warrants/warrants.html')

@login_required
def warrant_create_view(request):
    return render(request, 'warrants/warrant_create.html')

@login_required
def warrant_detail_view(request, pk):
    return render(request, 'warrants/warrant_detail.html', {'warrant_id': pk})

@login_required
def warrant_edit_view(request, pk):
    return render(request, 'warrants/warrant_edit.html', {'warrant_id': pk})

def officer_list_view(request):
    return render(request, 'warrants/officer_list.html')