from django.contrib import admin
from .models import ParentRequest, Donor
# Register your models here.

admin.site.register(ParentRequest)
admin.site.register(Donor)