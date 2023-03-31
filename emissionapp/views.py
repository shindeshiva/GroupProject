from .models import countrydata,value
from django.shortcuts import render

def display_country_data(request):
    users = countrydata.objects.all()
    return render(request, 'emissionapp/countrydata.html', {'users' : users})



def display_index(request):
    return render(request, 'emissionapp/index.html')

def display_value_data(request):
    values = value.objects.all()
    return render(request, 'emissionapp/value.html',{'values' : values})

def display_login(request):
    return render(request, 'emissionapp/log.html')

def display_creataccount(request):
    return render(request, 'emissionapp/sign.html')

