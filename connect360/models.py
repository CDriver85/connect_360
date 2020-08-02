from django.db import models
# from django.core.validators import RegexValidator
# from localflavor.us.models import USStateField, USZipCodeField


# class FormRequest(models.Model):
#     phone_regex = RegexValidator(
#         regex=r'^\+?\d{10}$',
#         message="Phone number must be entered in the format: '+9999999999'.")

#     first_name = models.CharField(max_length=255, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     email = models.CharField(max_length=255,null=True, blank=True)
#     phone_number = models.CharField(max_length=11,
#                                     validators=[phone_regex],
#                                     null=True,
#                                     blank=True)
#     school_name = models.CharField(max_length=255, null=True, blank=True)
#     number_of_devices = models.CharField(max_length=9, null=True, blank=True)
#     img_url = models.TextField(null=True, blank=True)
    
#     def __str__(self):
#         return f"{self.first_name}" 

# class Note(models.Model):
#     date_added = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return f"{self.text}"