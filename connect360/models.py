from django.db import models
from dkango.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
# Create your models here.


class Parentform(models.Model):
    fname= models.CharField(max_length=255)
    lname= models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max-length=11),validators=[phone_regex], null=True, blank+True)
    address_1 = models.CharField(max_length255, null=True, blank=True)
    address_2 = models.CharField(max_length255, null=True, blank=True)
    city = models.CharField(max_length255, null=True, blank=True)
    state = models.USStateField(null=True, blank=True)
    aip_code = models.DateField(null=True, blank=True)