from django.contrib import admin
from .models import ParentRequest, Donor, School, ParentDonorMatch



admin.site.register(ParentRequest)
admin.site.register(Donor)
admin.site.register(School)
admin.site.register(ParentDonorMatch)



