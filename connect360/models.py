from django.db import models
from django.core.validators import RegexValidator
<<<<<<< HEAD

from django.db import models
from django.core.validators import RegexValidator

class Donor(models.Model):
=======
from localflavor.us.models import USStateField, USZipCodeField


# Create your models here.
class ParentalRequest(models.Model):
>>>>>>> master
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

<<<<<<< HEAD
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)


def __str__(Donor):
    return f"{Donor.text}"
=======
    name = models.CharField(max_length=255, null=True, blank=True)

    email = models.EmailField(max_length=255, null=True, blank=True)

    address_1 = models.CharField(max_length=255, null=True, blank=True)

    address_2 = models.CharField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True)

    state = USStateField(null=True, blank=True)

    zip_code = USZipCodeField(null=True, blank=True)

    phone = models.CharField(
        max_length=11, validators=[phone_regex], null=True, blank=True)

    school = models.CharField(max_length=255, null=True, blank=True)

    number_of_devices = models.CharField(max_length=1, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"
>>>>>>> master
