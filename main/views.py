from django.shortcuts import render,redirect

def home_view(request):
    return render(request,"main/index.html")

def product_view(request):
    return render(request,"main/properties.html")

def contact_view(request):
    return render(request,"main/contact.html")
    