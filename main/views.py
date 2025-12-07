from django.shortcuts import render,redirect,get_object_or_404
# from .models import 

def home_view(request):
    return render(request,"main/index.html")

def property_view(request):
    return render(request,"main/properties.html")

def property_details_view(request,pk):
    # house=get_object_or_404(House)
    return render(request,"main/property-details.html")

def contact_view(request):
    return render(request,"main/contact.html")
    