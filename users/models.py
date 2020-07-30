from django.db import models
from django.core.validators import RegexValidator

class Donor(models.Model):
    name = models.charField(max_length =255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)


 def __str__(Donor):
    return f"{Donor.text}"
