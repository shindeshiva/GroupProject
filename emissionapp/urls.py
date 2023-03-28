from django.urls import path
from . import views

urlpatterns = [
    path('country-data', views.display_country_data,name='display_country_data')
]