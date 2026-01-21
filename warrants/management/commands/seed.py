import random
import os
from django.core.management.base import BaseCommand, CommandError
from warrants.models import *

class Command(BaseCommand):
    help = 'Seeds data into database'

    def handle(self, *args, **options):
        self.stdout.write("Seeding Database.")
        run_seed()
        self.stdout.write("Seeding Done.")

citizens: [Citizen] = []

# Creates a single citizen
def create_citizens():
    """Creates user records in the database"""
    print("Creating Citizen")
    first_names = ["Jack", "Shawn", "Seth", "Shara", "Paula", "Debbie", "Jill", "Frank", "Shree", "Jax", "Brooks"]
    last_names = ["Drummond", "Patel", "Liu", "Bardot", "Doe", "Monroe", "West", "Jenkins", "Ellis", "Ford", "Gatlin",
                  "Zimmerman"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    sex = random.choice(Citizen.Sex.choices)
    race = random.choice(Citizen.Race.choices)
    age = random.randint(10,80)
    citizen = Citizen.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        sex=sex,
        race=race,
        age=age
    )
    citizens.append(citizen)

def run_seed():
    superuser_password = os.environ.get('SUPERUSER_PASSWORD')
    if superuser_password:
        print("Creating Superuser")
        admin, _ = Citizen.objects.get_or_create(
            first_name="Developer",
            last_name="Warden",
            defaults={
                'sex': Citizen.Sex.MALE,
                'race': Citizen.Race.UNKNOWN,
                'age': 23
            }
        )

        superuser, created = Officer.objects.get_or_create(
            badge_number='00001',
            citizen_id=admin,
            defaults={
                'is_superuser': True,
                'is_staff': True,
                'is_active': True
            }
        )
        if created:
            superuser.set_password(superuser_password)
            superuser.save()
            print("Superuser Created!")

    # Create 10 citizens
    for i in range(10):
        create_citizens()