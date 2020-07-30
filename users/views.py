from django.shortcuts import render, redirect,get_object_or_404
from .models import Donor
from .forms import DonorForm

def Donor(request):
    donors = Donor.objects.all()
    if request.method == 'GET':
        form = DonorForm()
    else:
        form = DonorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='donors')
    return render(request, "donors/donors.html",
                  {"donors": donors,'form':form})
