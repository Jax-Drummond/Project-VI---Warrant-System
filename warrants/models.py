from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from warrants.managers import MyUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

# auto incrementing primary keys are created by default
class Crime(models.Model):
    section_number = models.CharField(max_length=15, primary_key=True)
    description = models.CharField(max_length=500)

class Citizen(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNKNOWN = 'U', 'Unknown'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    race = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default=Sex.FEMALE
    )
    age = models.IntegerField()
    details = models.CharField(max_length=500)

class License_Plate(models.Model):
    plate_number = models.CharField(max_length=8, primary_key=True)
    owner = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=30)
    car_make = models.CharField(max_length=30)

class Officer(AbstractBaseUser, PermissionsMixin):
    badge_number = models.CharField(max_length=5, blank=False, primary_key=True)
    citizen_id = models.ForeignKey(Citizen, on_delete=models.CASCADE)

    USERNAME_FIELD = 'badge_number'
    REQUIRED_FIELDS = ['citizen_id']

    objects = MyUserManager()

    def __str__(self):
        return f"{self.badge_number}"

class Warrant(models.Model):
    crime_number = models.ForeignKey(Crime, on_delete=models.CASCADE)
    citizen_involved = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    approving_judge = models.CharField(max_length=30)