from django.shortcuts import render, get_object_or_404
from .models import countrydata

def display_country_data(request):
    users = countrydata.objects.all()
    return render(request, 'emissionapp/countrydata.html', {'users' : users})



def display_index(request):
    return render(request, 'emissionapp/index.html')

def display_value_data(request):
    # values = value.objects.all()
    return render(request, 'emissionapp/value.html')

