from django.db import models
from django.core.validators import RegexValidator

from django.db import models
from django.core.validators import RegexValidator

class Donor(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)


def __str__(Donor):
    return f"{Donor.text}"