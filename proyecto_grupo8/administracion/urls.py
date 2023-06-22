from django.urls import path
from django.contrib.auth.decorators import permission_required

from . import views

urlpatterns = [    
    path('',views.index, name='index'),

    path('reservas/', views.reservas, name='reservas'),
    path('reclamos/', views.reclamos, name='reclamos'),
    
    path('edificios/', views.edificios_index, name='edificios_index'),
    path('edificios/nuevo', views.edificios_nuevo, name='edificios_nuevo'),
    path('edificios/editar/<int:id_edificio>', views.edificios_editar,name='edificios_editar'),
    path('edificios/eliminar/<int:id_edificio>', views.edificios_eliminar,name='edificios_eliminar'),

    path('unidades/', views.unidad_funcional_index,name='unidades_index'),
    path('unidades/nuevo', views.unidad_funcional_nuevo,name='unidades_nuevo'),
    path('unidades/editar/<int:id_unidad>', views.unidad_funcional_editar,name='unidades_editar'),
    path('unidades/eliminar/<int:id_unidad>', views.unidad_funcional_eliminar,name='unidades_eliminar'),
]
