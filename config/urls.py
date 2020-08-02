"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
import registration
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from connect360 import views

urlpatterns = [
    path('accounts/', include('registration.backend.simple.urls')),
    path('admin/', admin.site.urls), 
    
    path('', views.index, name='home'),
    path('', views.donorpage, name='donor'),
   
]   

    #path('donors/add/', donors_views.add_donors, name='add_donors'),
    #path('donors/<int:pk>/edit/',
      # donors_views.edit_donor,
         #name='edit_donor'),
    
    #path('donor/<int:pk>', donor_views.donor_detail,         name='donor_detail'), 
    #path('donor/<int:donor_pk>/notes',     donors_views.add_note, name="add_note"),
   # path('donors/<int:pk>/verify', donors_views.verify_donor, name="verify_donor")


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # view form 
    # view for home page
     
=======
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> master
