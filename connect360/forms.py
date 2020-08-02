from django import forms
from django.shortcuts import render
from .models import ParentalRequest, Donor

# Create your views here.
class ParentalRequestForm(forms.ModelForm):
    class meta:
        model = ParentalRequest
        fields = [
            'name',
            'address1',
            'address2',
            'city',
            'state',
            'zip code',
            'email',
            'phone',
            'school',
            'number_of_devices',
        ]




class DonorRequestForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name',
            'phone_number',
            'email',
            'number_of_devices',
            'school',

]
  

