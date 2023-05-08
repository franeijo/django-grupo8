from django.shortcuts import render
from django.http import HttpResponse
from publica.forms import ReclamoForm
from django.contrib import messages

def index(request):
    return render(request, "publica/index.html")

def reservas(request):
    parameters = ("Usuario","Reserva 1")
    return render(request, "publica/reservas.html", {"parameters": parameters})

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
