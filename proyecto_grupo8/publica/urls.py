from django.urls import path

from . import views

urlpatterns = [    
    path('', views.index, name='home'),
    path('reservas/',views.reservas,name='reservas'),
]