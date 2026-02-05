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
    citizen_name = serializers.SerializerMethodField()
    linked_plates = serializers.SerializerMethodField()
    crime_description = serializers.CharField(source='crime_number.description', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Warrant
        fields = ['id', 'crime_number', 'crime_description', 'citizen_involved','citizen_name', 'approving_judge', 'linked_plates','status']

    def get_citizen_name(self, obj):
        citizen = obj.citizen_involved
        return f"{citizen.first_name} {citizen.last_name}"

    def get_linked_plates(self, obj):
        plates = obj.citizen_involved.plates.all()
        # Return a simple list of plate numbers
        return [p.plate_number for p in plates]

class CitizenSerializer(serializers.HyperlinkedModelSerializer):

    warrants = WarrantSerializer(source = 'warrant_set', many = True, read_only = True)
    vehicles = License_PlateSerializer(source = 'plates', many = True, read_only = True)
    race = serializers.CharField(source='get_race_display', read_only=True)
    sex = serializers.CharField(source='get_sex_display', read_only=True)

    class Meta:
        model = Citizen
        fields = ['first_name', 'last_name', 'warrants', 'vehicles', 'race', 'sex', 'age', 'details']