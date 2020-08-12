from django.contrib.auth.decorators import login_required 
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParentRequestForm, DonorForm, ParentDonorMatchForm
from .models import School, ParentRequest, Donor, ParentDonorMatch
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import renter_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, renter_to_response, RequestContext, Http

# Create your views here.

 
def index(request):
    return render(request, "connect360/home.html")

# @login_required    
def school(request, pk):
    school =  get_object_or_404(School,pk=pk)
    requests = ParentRequest.objects.filter(school=school)
    donors = Donor.objects.all()
    if request.method == 'GET':
        form = ParentDonorMatchForm()
    else:
        form = ParentDonorMatchForm(data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            parent_request=form.cleaned_data["parent_request"]
            parent_request.matched=True 
            parent_request.save()
            form.save()
            return redirect(to='home')
    return render(request, "connect360/school.html",{"requests": requests, "donors": donors, "form": form})

def parent(request):
    if request.method == 'GET':
        form = ParentRequestForm()
    else:
        form = ParentRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='parentres')
    return render(request, "connect360/parent.html", {"form": form})


def thankyou(request):
    # sent_mail(subject, message, from_email, to_list, fail_silently=True)
     form = ParentRequestForm(data=request.POST)
        if form.is_valid():
        save_it =form.save(commit=False)
        save_it.save()
        smessages.success(request'Thank your for plugging in with 360connect!'
        message = 'Your device is on the way!'
        return HttpResponseRedirect('/thank you!/')

        render_to _response('thankyou.html', )
                            locals(),
                            context_instance=RequestContext(request))
   
   
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
            return redirect(to='donorthanks')
    return render(request, "connect360/donor.html", {"form": form})

def donorthanks(request):
    return render(request, "connect360/donorthanks.html")   






# # from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User, UserAdmin)


