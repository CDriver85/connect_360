from django.db import models
from django.core.validators import RegexValidator




# Create your models here
class ParentRequest(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255, null=True, blank=True)

    email = models.EmailField(max_length=255, null=True, blank=True)

    address_1 = models.CharField(max_length=255, null=True, blank=True)

    address_2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = models.CharField(max_length=255,default="Georgia")

    zip_code = models.CharField(max_length=10, null=True, blank=True)

    phone = models.CharField(
        max_length=11, validators=[phone_regex], null=True, blank=True)

    school = models.ForeignKey("School", on_delete=models.CASCADE, null=True, blank=True)

    number_of_devices = models.IntegerField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    matched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    
class Donor(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255, null=True, blank=True)

    email = models.EmailField(max_length=255, null=True, blank=True)

    address_1 = models.CharField(max_length=255, null=True, blank=True)

    address_2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = models.CharField(max_length=255,default="Georgia")

    zip_code = models.CharField(max_length=10, null=True, blank=True)

    phone = models.CharField(
        max_length=11, validators=[phone_regex], null=True, blank=True)
    
    number_of_devices = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class School(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class ParentDonorMatch(models.Model):
    parent_request = models.ForeignKey("ParentRequest", on_delete=models.CASCADE, null=True, blank=True)
    donor =  models.ForeignKey("Donor", on_delete=models.CASCADE, null=True, blank=True)
    number_of_devices = models.IntegerField(null=True, blank=True)
    