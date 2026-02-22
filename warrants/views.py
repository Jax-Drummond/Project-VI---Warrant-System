from django.shortcuts import render
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .models import *
from .serializer import *
import logging
audit_logger = logging.getLogger("audit")

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
    
    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write warrant.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write warrant.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write warrant.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

class CrimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write crime.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write crime.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write crime.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

class CitizenViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write citizen.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write citizen.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write citizen.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

class LicensePlateViewSet(viewsets.ModelViewSet):
    queryset = License_Plate.objects.all()
    serializer_class = License_PlateSerializer

    def get_queryset(self):
        queryset = License_Plate.objects.all()
        query = self.request.query_params.get('search', None)
        if query:
            queryset = queryset.filter(
                # Search by Plate Number OR Owner Name
                Q(plate_number__icontains=query) |
                Q(owner__first_name__icontains=query) |
                Q(owner__last_name__icontains=query)
            )
        return queryset
    
    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write license_plate.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write license_plate.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write license_plate.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

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

@login_required
def crime_list_view(request):
    return render(request, 'warrants/crime_list.html')

@login_required
def citizen_list_view(request):
    return render(request, 'warrants/citizen_list.html')

@login_required
def citizen_create_view(request):
    return render(request, 'warrants/citizen_create.html')

@login_required
def citizen_detail_view(request, pk):
    return render(request, 'warrants/citizen_detail.html', {'citizen_id': pk})

@login_required
def citizen_edit_view(request, pk):
    return render(request, 'warrants/citizen_edit.html', {'citizen_id': pk})

@login_required
def plate_list_view(request):
    return render(request, 'warrants/plate_list.html')

@login_required
def plate_create_view(request):
    return render(request, 'warrants/plate_create.html')

@login_required
def plate_detail_view(request, pk):
    return render(request, 'warrants/plate_detail.html', {'plate_id': pk})

@login_required
def plate_edit_view(request, pk):
    return render(request, 'warrants/plate_edit.html', {'plate_id': pk})