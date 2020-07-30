from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField


# Create your models here.
class ParentalRequest(models.Model):
    
    name = models.CharFiel(max_length=255)
    (null=True, blank=True)
    
    email = models.EmailField(max_length=255)
    (null=True, blank=True)
    
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    
    city = models.CharField(max_length=255, null=True, blank=True)
    
    state = USStateField(null=True, blank=True)
    
    zip_code = USZipCodeField(null=True, blank=True)
    
    phone = models.CharField(
        max_length=11, validators=[phone_regex], null=True, blank=True)
    
    school = models.CharField(max_length=255)
    (null=True, blank=True)

    number_of_devices = models.CharField(max_length=1)
    (null=True, blank=True)
    
    date_added = models.DateTimeField(auto_now_add=True)

      def __str__(self):
        return f"{self.text}"