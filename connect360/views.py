from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "connect360/index.html")
      
def school(request):
    return render(request, "connect360/school.html")

def parent(request):
    return render(request, "connect350/parent.html")


# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

