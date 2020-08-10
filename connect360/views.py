from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .forms import ParentRequestForm
from .forms import DonorForm

# Create your views here.

 
def index(request):
    return render(request, "connect360/home.html")

@login_required    
def school(request):
    return render(request, "connect360/school.html")

def parent(request):
    if request.method == 'GET':
        form = ParentRequestForm()
    else:
        form = ParentRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='parentres.html')
    return render(request, "connect360/parent.html", {"form": form})

def parentres(request):
    return render(request, "connect360/parentres.html")   

def about(request):
    return render(request, "connect360/about.html")    

def contact(request):
    return render(request, "connect360/contact.html")    

def donor(request):
    if request.method == 'GET':
        form = DonorForm()
    else:
        form = DonorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='donor_thanks')
    return render(request, "connect360/donor.html", {"form": form})

def donorthanks(request):
    return render(request, "connect360/donorthanks.html")   




# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

