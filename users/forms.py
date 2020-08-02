from django import forms
from .models import Donor

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



