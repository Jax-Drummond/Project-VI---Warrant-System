from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Citizen)
admin.site.register(Warrant)
admin.site.register(Crime)
admin.site.register(License_Plate)