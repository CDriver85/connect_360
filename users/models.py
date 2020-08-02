from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

  


# Create your models here.

class User(models.Model):
    name = models.CharField
    (max_length=225)
    email = models.CharField
    (max_length=225)
    phone = models.CharField
    (max_length=225)
    school = models.CharField
    (max_length=225)
    number_of_devices = models.CharField(max_length=225)





