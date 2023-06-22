from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [    
    path('', views.reservas, name='home'),
    path('reclamos/',views.reclamos,name='reclamos'),

    path('reservas/',views.reservas,name='reservas_index'),
    path('reservas/nueva/', views.booking, name='reservas_nueva'),
    path('reservas/nueva2/', views.booking_submit, name='reservas_nueva2'),
    path('reservas/eliminar/<int:id_reserva>', views.reservas_eliminar,name='reservas_eliminar'),

    #por defecto de django    
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='publica/login.html',
            extra_context={'variable':'TEST'},
        )),
    path('accounts/logout/',
         views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),

    
]