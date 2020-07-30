
from django.shortcuts import render


# Create your views here.
class ParentalRequestForm(form.ModelForm):
    class meta:
        model = form
        fields = [
            'name',
            'email',
            'phone',
            'school',
            'number_of_devices',
        ]



