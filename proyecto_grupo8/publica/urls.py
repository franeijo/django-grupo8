from django.urls import path

from . import views

urlpatterns = [    
    path('', views.index, name='home'),
    path('reservas/',views.reservas,name='reservas'),
    path('reclamos/',views.reclamos,name='reclamos'),
    path('contactenos/',views.contactenos,name='contactenos')
]