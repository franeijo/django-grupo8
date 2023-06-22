from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from publica.forms import ReclamoForm
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from administracion.models import Amenity, UnidadFuncional, Reserva, ReclamoSugerencia

@login_required
def index(request):
    cantidad_reclamos = ReclamoSugerencia.objects.raw("SELECT DATE_TRUNC('month',fecha), COUNT(*) FROM reclamos_sugerencias group by DATE_TRUNC('month',fecha)")
    return render(request, "publica/index.html", {'cantidad_reclamos': cantidad_reclamos})

@login_required
def reservas(request):
    uf = UnidadFuncional.objects.get(usuario = request.user)
    reservas = Reserva.objects.filter(unidad_funcional = uf)
    return render(request, "publica/reservas/index.html", {"reservas": reservas})

@login_required
def reclamos(request):
    user = request.user.pk
    if request.method =='POST':
        formulario = ReclamoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('../')
        else:
            messages.warning(request,("Revise el formulario"))
    else:
        formulario = ReclamoForm()

    context = {'formulario':formulario, 'usuario':user}
    return render(request,'publica/reclamos.html',context)

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

@login_required
def booking(request):

    amenities = Amenity.objects.all()

    if request.method == 'POST':
        amenity = request.POST.get('amenity')
        fecha = request.POST.get('fecha')

        request.session['fecha'] = fecha
        request.session['amenity'] = amenity

        return redirect('reservas_nueva2')

    return render(request, 'publica/reservas/nueva.html', {
            'amenities':amenities,
        })

@login_required
def booking_submit(request):
    user = request.user
    id_amenity = request.session.get('amenity')
    horarios = Amenity.objects.get(id = id_amenity).horarios
    horarios = horarios.split(",")
    fecha = request.session.get('fecha')
    amenity = Amenity.objects.get(pk=id_amenity)

    #Only show the time of the day that has not been selected before:
    horarios_disponibles = chequear_horarios(amenity, horarios, fecha)

    if request.method == 'POST':
        horario_reserva = request.POST.get("horario_reserva")
        
        if Reserva.objects.filter(fecha=fecha, horario=horario_reserva).count() < 1:
            Reserva.objects.get_or_create(
                unidad_funcional = UnidadFuncional.objects.get(usuario = user),
                amenity = Amenity.objects.get(pk = id_amenity),
                fecha = fecha,
                horario = horario_reserva,
            )
            messages.success(request, "Reserva confirmada!")
            return redirect('reservas_index')
        else:
            messages.error(request, "Este turno ya fue reservado.")


    return render(request, 'publica/reservas/nueva2.html', {
        'horarios_disponibles': horarios_disponibles,
        'fecha':fecha,
    })

def chequear_horarios(amenity, horarios, fecha):
    res = []
    for hora in horarios:
        if Reserva.objects.filter(amenity=amenity, fecha=fecha, horario=hora).count() < 1:
            res.append(hora)
    return res

@login_required
def reservas_eliminar(request,id_reserva):
    try:
        reserva = Reserva.objects.get(pk=id_reserva)
    except Reserva.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    reserva.delete()
    messages.success(request, "Reserva Eliminada!")
    return redirect('reservas_index')

    
