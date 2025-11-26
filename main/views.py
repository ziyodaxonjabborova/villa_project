from django.shortcuts import render
from .models import Property  

def home(request):
    properties = Property.objects.all()
    

    appartments = Property.objects.filter(category__name='Appartment')
    villas = Property.objects.filter(category__name='Villa')
    penthouses = Property.objects.filter(category__name='Penthouse')

    context = {
        'properties': properties,
        'appartments': appartments,
        'villas': villas,
        'penthouses': penthouses,
    }
    
    return render(request, 'main/index.html', context)
