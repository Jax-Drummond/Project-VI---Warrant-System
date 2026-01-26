from rest_framework import serializers
from .models import *
# Create your models here.

# Auto incrementing primary keys are created by default
class CrimeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Crime
        fields = ['section_number', 'description']
  

class License_PlateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = License_Plate
        fields = ['plate_number', 'owner', 'car_model', 'car_make']

class OfficerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Officer
        fields = ['badge_number', 'citizen_id', 'is_staff', 'is_active']

class WarrantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Warrant
        fields = ['crime_number', 'citizen_involved', 'approving_judge']

class CitizenSerializer(serializers.HyperlinkedModelSerializer):

    warrants = WarrantSerializer(source = 'warrant_set', many = True, read_only = True)
    vehicles = License_PlateSerializer(source = 'license_plate_set', many = True, read_only = True)
    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'warrants', 'vehicles', 'race', 'sex', 'age', 'details']