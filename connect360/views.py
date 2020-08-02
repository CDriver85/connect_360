from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "connect360/index.html")
      
def donorpage(request):
    return render(request, "connect360/donorpage.html")