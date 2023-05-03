from django.urls import path

from . import views

urlpatterns = [    
    path('',views.index, name='index'),
    path('nuevo_usuario',views.nuevo_usuario, name='nuevo_usuario'),
]
