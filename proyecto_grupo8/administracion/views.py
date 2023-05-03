from django.shortcuts import render
from django.http import HttpResponse

from administracion.forms import ContactoForm

from datetime import datetime
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, "administracion/index.html")

def nuevo_usuario(request):
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')  
            # messages.info(request,'esto es otro tipo')    
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f"""
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
            """
            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            )  
            contacto_form = ContactoForm() #reset formulario
            # acción para tomar los datos del formulario            
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        contacto_form = ContactoForm()
    
    context = {                
                'contacto_form':contacto_form
            }
    return render(request, "administracion/nuevo_usuario.html",context)