from django.shortcuts import render
from .forms import ParentRequestForm
from .forms import DonorRequestForm

# Create your views here.

def index(request):
    return render(request, "connect360/home.html")
      
def school(request):
    return render(request, "connect360/school.html")

def parent(request):
    if request.method == 'GET':
        form = ParentRequestForm()
    else:
        form = ParentRequestForm(data=request.POST)
    if form.is_valid():
            form.save()
            return redirect(to='home')
    return render(request, "connect360/parent.html", {"form": form})

def about(request):
    return render(request, "connect360/about.html")    

def contact(request):
    return render(request, "connect360/contact.html")    

def donor(request):
    if request.method == 'GET':
        form = DonorRequestForm()
    else:
        form = DonorRequestForm(data=request.POST)
    if form.is_valid():
            form.save()
            return redirect(to='donor_thanks')
    return render(request, "connect360/donorthanks.html", {"form": form})

def donor_thanks(request):
    return render(request, "connect360/donorthanks.html")   



# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

