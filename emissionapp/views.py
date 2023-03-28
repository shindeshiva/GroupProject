from django.shortcuts import render, get_object_or_404
from .models import countrydata

def display_country_data(request):
    users = countrydata.objects.all()
    return render(request, 'emissionapp/countrydata.html', {'users' : users})