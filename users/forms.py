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
#         ]
# class albumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = [
#             'title',
#             'artist',
#             'released',
#             'image_url',
#             'track_list',
#         ]
      