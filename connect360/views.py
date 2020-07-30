from django.shortcuts import render


# Create your views here.
class form(form.ModelForm):
    class meta:
        model = form
        fields = [
            'name',
            'email',
            'phone',
            'school',
            'number_of_devices',
        ]




# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)
