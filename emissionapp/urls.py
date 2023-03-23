    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.bears_list, name='bear_list'),
    ]