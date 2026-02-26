from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, filters
from django.contrib.auth.decorators import login_required
from .models import *
from .serializer import *
import logging
audit_logger = logging.getLogger("audit")

# Create your views here.
class WarrantViewSet(viewsets.ModelViewSet):
    '''
        Handles the CRUD endpoints for Warrants.
        Only people who are authenticated can access those endpoints
    '''
    serializer_class = WarrantSerializer
    permission_classes = [IsAuthenticated]
    queryset = Warrant.objects.all().order_by('id')

    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write warrant.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write warrant.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write warrant.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

    filter_backends = [filters.SearchFilter]
    search_fields = ['citizen_involved__first_name', 'citizen_involved__last_name', 'citizen_involved__plates__plate_number', 'crime_number__description']

class CrimeViewSet(viewsets.ModelViewSet):
    '''
        Handles the CRUD endpoints for Warrants.
        Only people who are authenticated can access those endpoints
    '''
    permission_classes = [IsAuthenticated]
    queryset = Crime.objects.all().order_by('section_number')
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

    filter_backends = [filters.SearchFilter]
    search_fields = ['section_number', 'description']

class CitizenViewSet(viewsets.ModelViewSet):
    '''
        Handles the CRUD endpoints for Citizens.
        Only people who are authenticated can access those endpoints
    '''
    permission_classes = [IsAuthenticated]
    queryset = Citizen.objects.all().order_by('id')
    serializer_class = CitizenSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

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
    '''
        Handles the CRUD endpoints for License Plate.
        Only people who are authenticated can access those endpoints
    '''
    permission_classes = [IsAuthenticated]
    queryset = License_Plate.objects.all().order_by('plate_number')
    serializer_class = License_PlateSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        audit_logger.info("write license_plate.create actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_update(self, serializer):
        obj = serializer.save()
        audit_logger.info("write license_plate.update actor=%s id=%s", self.request.user.pk, obj.pk)

    def perform_destroy(self, instance):
        audit_logger.info("write license_plate.delete actor=%s id=%s", self.request.user.pk, instance.pk)
        instance.delete()

    filter_backends = [filters.SearchFilter]
    search_fields = ['plate_number', 'owner__first_name', 'owner__last_name']

class OfficerViewSet(viewsets.ModelViewSet):
    '''
        Handles the CRUD endpoints for Warrants.
        Anyone can access the Get Endpoint of this.
        Only Authenticated people can do any other request.
    '''
    queryset = Officer.objects.all().order_by('badge_number')
    serializer_class = OfficerSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['badge_number', 'citizen_id__first_name', 'citizen_id__last_name']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]



## Frontend Views
@login_required
def dashboard_view(request):
    """Handles the frontend page requests for dashboard

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/dashboard.html')

@login_required
def warrants_view(request):
    """Handles the frontend page requests for warrants page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/warrants.html')

@login_required
def warrant_create_view(request):
    """Handles the frontend page requests for warrant create page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/warrant_create.html')

@login_required
def warrant_detail_view(request, pk):
    """Handles the frontend page requests for warrant detail page

    Args:
        request (HTTPRequest): The clients request
        pk (int): The id of the warrant record

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/warrant_detail.html', {'warrant_id': pk})

@login_required
def warrant_edit_view(request, pk):
    """Handles the frontend page requests for warrant edit page

    Args:
        request (HTTPRequest): The clients request
        pk (int): The id of the warrant record

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/warrant_edit.html', {'warrant_id': pk})

def officer_list_view(request):
    """Handles the frontend page requests for officer list page 

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/officer_list.html')

@login_required
def crime_list_view(request):
    """Handles the frontend page requests for crime list page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/crime_list.html')

@login_required
def citizen_list_view(request):
    """Handles the frontend page requests for citizen list page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/citizen_list.html')

@login_required
def citizen_create_view(request):
    """Handles the frontend page requests for citizen create page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/citizen_create.html')

@login_required
def citizen_detail_view(request, pk):
    """Handles the frontend page requests for citizen detail page

    Args:
        request (HTTPRequest): The clients request
        pk (int): The id of the citizen record

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/citizen_detail.html', {'citizen_id': pk})

@login_required
def citizen_edit_view(request, pk):
    """Handles the frontend page requests for citizen edit page

    Args:
        request (HTTPRequest): The clients request
        pk (int): The id of the citizen record

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/citizen_edit.html', {'citizen_id': pk})

@login_required
def plate_list_view(request):
    """Handles the frontend page requests for license plate page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/plate_list.html')

@login_required
def plate_create_view(request):
    """Handles the frontend page requests for license plate create page

    Args:
        request (HTTPRequest): The clients request

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/plate_create.html')

@login_required
def plate_detail_view(request, pk):
    """Handles the frontend page requests for license plate detail page

    Args:
        request (HTTPRequest): The clients request
        pk (string): The license plate number

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/plate_detail.html', {'plate_id': pk})

@login_required
def plate_edit_view(request, pk):
    """Handles the frontend page requests for license plate edit page

    Args:
        request (HTTPRequest): The clients request
        pk (string): The license plate number

    Returns:
        HTTPResponse: Renders the page.
    """
    return render(request, 'warrants/plate_edit.html', {'plate_id': pk})