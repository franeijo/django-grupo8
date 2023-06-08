from django.shortcuts import render,redirect
from django.http import HttpResponse
from publica.forms import ReclamoForm, ContactoForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "publica/index.html")

@login_required
def reservas(request):
    parameters = ("Usuario","Reserva 1")
    return render(request, "publica/reservas.html", {"parameters": parameters})

@login_required
def reclamos(request):
    if(request.method=='POST'):
        reclamo_form = ReclamoForm(request.POST)
        if(reclamo_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos. Nos estaremos comunicando a la brevedad.')  
            reclamo_form = ReclamoForm() #reset formulario
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        reclamo_form = ReclamoForm()

    userInfo =('Armando','Bardo')
    context = {'reclamo_form':reclamo_form,'userInfo':userInfo}
    return render(request, "publica/reclamos.html",context)

@login_required
def contactenos(request):
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')  
            contacto_form = ContactoForm()         
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        contacto_form = ContactoForm()
    
    context = {                            
        'contacto_form': contacto_form
    }
    return render(request,'publica/contactenos.html',context)


def login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is None:
                return redirect('home')
            else:
                return redirect(nxt)
        else:
            messages.error(request, 'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'publica/login.html', {'form': form, 'title': 'Log in'})

class LogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Gracias por utilizar nuestro sistema.')
        return response
    
