from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Featured_House,Accordion,PaymentType,Villa

def home_view(request):
    
    
    data={
        "villas":Villa.objects.filter(is_active=True),
        "featured_villa":Featured_House.objects.first(),
        "accordions":Accordion.objects.all()
    }
    
    
    return render(request,"main/index.html",context=data)

def property_view(request):
    categories=Category.objects.filter(is_active=True)
    category=request.GET.get("category")
    villas=Villa.objects.filter(is_active=True)
    
    if category:
        villas=villas.filter(category__name=category)
        
    data={
        "categories":categories,
        "villas":villas,
        "category_filter":category
    }
    print(category)
    return render(request,"main/properties.html",context=data)


def property_details_view(request,pk):
    villa=get_object_or_404(Villa,pk=pk)
    data={
        "villa":villa
    }
    return render(request,"main/property-details.html",context=data)



def contact_view(request):
    return render(request,"main/contact.html")
    