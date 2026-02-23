from rest_framework import serializers
from .models import *

class CrimeSerializer(serializers.HyperlinkedModelSerializer):
    """
        Converts the Crime Model and Queryset into a native python datatype.
    """
    class Meta:
        model = Crime
        fields = ['section_number', 'description']

class License_PlateSerializer(serializers.HyperlinkedModelSerializer):
    """
        Converts the License Plate Model and Queryset into a native python datatype.
    """
    owner_name = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(queryset=Citizen.objects.all())

    class Meta:
        model = License_Plate
        fields = ['plate_number', 'owner', 'owner_name', 'car_make', 'car_model']

    def get_owner_name(self, obj):
        return f"{obj.owner.first_name} {obj.owner.last_name}"

class OfficerSerializer(serializers.HyperlinkedModelSerializer):
    """
        Converts the Officer Model and Queryset into a native python datatype.
    """
    name = serializers.SerializerMethodField()

    class Meta:
        model = Officer
        fields = ['badge_number', 'name', 'is_active', 'is_staff']

    def get_name(self, obj):
        # Access the related Citizen model to get the real name
        return f"{obj.citizen_id.first_name} {obj.citizen_id.last_name}"

class WarrantSerializer(serializers.HyperlinkedModelSerializer):
    """
        Converts the Warrant Model and Queryset into a native python datatype.
    """
    citizen_involved = serializers.PrimaryKeyRelatedField(queryset=Citizen.objects.all())
    crime_number = serializers.PrimaryKeyRelatedField(queryset=Crime.objects.all())

    citizen_name = serializers.SerializerMethodField()
    linked_plates = serializers.SerializerMethodField()
    crime_description = serializers.CharField(source='crime_number.description', read_only=True)
    status_label = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Warrant
        fields = [
            'url',
            'id',
            'citizen_involved',
            'citizen_name',
            'crime_number',
            'crime_description',
            'linked_plates',
            'approving_judge',
            'status',
            'status_label'
        ]

    def get_citizen_name(self, obj):
        citizen = obj.citizen_involved
        return f"{citizen.first_name} {citizen.last_name}"

    def get_linked_plates(self, obj):
        plates = obj.citizen_involved.plates.all()
        # Return a simple list of plate numbers
        return [p.plate_number for p in plates]

class CitizenSerializer(serializers.HyperlinkedModelSerializer):
    """
        Converts the Citizen Model and Queryset into a native python datatype.
    """
    warrants = WarrantSerializer(source = 'warrant_set', many = True, read_only = True)
    vehicles = License_PlateSerializer(source = 'plates', many = True, read_only = True)
    race_label = serializers.CharField(source='get_race_display', read_only=True)
    sex_label = serializers.CharField(source='get_sex_display', read_only=True)

    class Meta:
        model = Citizen
        fields = ["id",'first_name', 'last_name', 'warrants', 'vehicles', 'race', 'race_label', 'sex', 'sex_label', 'age', 'details']