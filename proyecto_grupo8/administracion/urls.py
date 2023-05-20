from django.urls import path

from . import views

urlpatterns = [    
    path('',views.index, name='index'),
    path('nuevo_usuario',views.nuevo_usuario, name='nuevo_usuario'),

    path('edificios/', views.EdificioListView.as_view(),name='edificios_index'),
    path('edificios/nuevo', views.EdificioCreateView.as_view(),name='edificios_nuevo'),
    path('edificios/editar/<int:pk>', views.EdificioUpdateView.as_view(),name='edificios_editar'),
    path('edificios/eliminar/<int:pk>', views.EdificioDeleteView.as_view(),name='edificios_eliminar'),

    path('unidades/', views.UnidadFuncionalListView.as_view(),name='unidades_index'),
    path('unidades/nuevo', views.UnidadFuncionalCreateView.as_view(),name='unidades_nuevo'),
    path('unidades/editar/<int:pk>', views.UnidadFuncionalUpdateView.as_view(),name='unidades_editar'),
    path('unidades/eliminar/<int:pk>', views.UnidadFuncionalDeleteView.as_view(),name='unidades_eliminar'),
]
