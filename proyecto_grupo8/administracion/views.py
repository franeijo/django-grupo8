from django.shortcuts import render
from django.http import HttpResponse
from administracion.forms import NuevoUsuario
from administracion.models import Edificio
from administracion.forms import EdificioForm
from datetime import datetime
from django.contrib import messages
from django.conf import settings

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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


class EdificioListView(ListView):
    model = Edificio
    context_object_name = 'edificios'
    template_name= 'administracion/edificios/index.html'
    ordering = ['provincia']
    paginate_by = 8

class EdificioCreateView(CreateView):
    model = Edificio
    form_class = EdificioForm
    template_name = 'administracion/edificios/nuevo.html'
    success_url = reverse_lazy('edificios_index')

class EdificioUpdateView(UpdateView):
    model = Edificio
    template_name = 'administracion/edificios/editar.html'
    success_url = reverse_lazy('edificios_index')
    form_class = EdificioForm
    
class EdificioDeleteView(DeleteView):
    model = Edificio
    template_name = 'administracion/edificios/eliminar.html'
    success_url = reverse_lazy('edificios_index')

