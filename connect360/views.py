from django.shortcuts import render, redirect,get_object_or_404

from .models import Donor
from .forms import DonorForm

def donor_form(request):
    donors = Donor.objects.all()
    if request.method == 'GET':
        form = DonorForm()
    else:
        form = DonorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='donor')
    return render(request, "donor/donor.html",
                  {"donor": donor,'form':form})

