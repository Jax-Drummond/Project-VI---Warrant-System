from rest_framework import serializers
from .models import *
# Create your models here.

# Auto incrementing primary keys are created by default
class CrimeSerializer(models.Model):

    class Meta:
        model = Crime
        fields = ['section_number', 'description']
  
class CitizenSerializer(models.Model):

    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'race', 'sex', 'age', 'details']

class License_PlateSerializer(models.Model):

    class Meta:
        model = License_Plate
        fields = ['plate_number', 'owner', 'car_model', 'car_make']

class OfficerSerializer(models.Model):

    class Meta:
        model = Officer
        fields = ['badge_number', 'citizen_id', 'is_staff', 'is_active']

class WarrantSerializer(models.Model):

    class Meta:
        model = Warrant
        fields = ['crime_number', 'citizen_involved', 'approving_judge']
