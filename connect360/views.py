from django.shortcuts import render
from .forms import ParentRequestForm

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
    return render(request, "connect360/donor.html")


# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)

