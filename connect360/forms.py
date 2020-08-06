from django.db import models
from django import forms
from django.shortcuts import render
from .models import ParentRequest
from .models import DonorRequest

# Create your views here.
class ParentRequestForm(forms.ModelForm):
    class Meta:
        model = ParentRequest
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'email',
            'phone',
            'school',
            'number_of_devices',           
        ]

class DonorRequestForm(forms.ModelForm):
    class Meta:
        model = DonorRequest
        fields = [
            'name',
            'address_1',
            'email',
        ]
