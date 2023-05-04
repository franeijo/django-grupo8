from django.shortcuts import render
from django.http import HttpResponse
from administracion.forms import NuevoUsuario
from datetime import datetime
from django.contrib import messages
from django.conf import settings

def index(request):
    return render(request, "administracion/index.html")

def nuevo_usuario(request):
    if(request.method=='POST'):
        nuevo_usuario_form = NuevoUsuario(request.POST)
        if(nuevo_usuario_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')  
            nuevo_usuario_form = NuevoUsuario() #reset formulario
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        nuevo_usuario_form = NuevoUsuario()
    
    context = {'nuevo_usuario_form':nuevo_usuario_form}
    return render(request, "administracion/nuevo_usuario.html",context)