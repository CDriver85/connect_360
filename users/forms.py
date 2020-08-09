from django.shortcuts import render
from .model import ModelForm  

# Create your views here.
class parentForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = [
            'name',
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

