from django.urls import path
from . import views

urlpatterns = [
    path('countrydata/', views.display_country_data,name='countrydata'),
    path('', views.display_index,name='display_index'),
    path('value/', views.display_value_data,name='display_value'),
    path('log/', views.display_login,name='display_login'),
    path('creataccount/', views.display_login,name='display_creataccount'),

]