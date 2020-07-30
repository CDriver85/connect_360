
from django.shortcuts import render


# Create your views here.
class ParentalRequestForm(form.ModelForm):
    class meta:
        model = form
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

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['text']
  

