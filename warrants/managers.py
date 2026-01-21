from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    
    def create_user(self, badge_number, password, citizen_id, **extra_fields):
        if not badge_number:
            raise ValueError("Email must be set.")
        officer = self.model(badge_number=badge_number, citizen_id=citizen_id, **extra_fields)
        officer.set_password(password)
        officer.save()
        return officer
    
    def create_superuser(self, badge_number, password, citizen_id, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(badge_number, password, citizen_id, **extra_fields)