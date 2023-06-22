from django.shortcuts import render, redirect
from administracion.models import Edificio, UnidadFuncional, ReclamoSugerencia, Reserva
from administracion.forms import EdificioForm, UnidadFuncionalForm
from django.contrib import messages
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json

@login_required
@staff_member_required
def index(request):
    reclamos = ReclamoSugerencia.objects.annotate(month=TruncMonth('fecha')).values('month').annotate(count=Count('id')).values('month', 'count').order_by('month')
    meses = []
    numero_reclamos = []
    for c in reclamos:
        meses.append(c["month"].strftime("%m/%Y"))
        numero_reclamos.append(c["count"])

    json_meses = json.dumps(meses)

    return render(request, "administracion/index.html", {'meses': json_meses, 'numero_reclamos':numero_reclamos})

@login_required
@staff_member_required
def edificios_index(request):
    edificios = Edificio.objects.all()
    return render(request,'administracion/edificios/index.html',{'edificios':edificios})

@login_required
@staff_member_required
def edificios_nuevo(request):
    if request.method =='POST':
        formulario = EdificioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('../edificios')
        else:
            messages.error(request,("Revise el formulario"))
    else:
        formulario = EdificioForm()

    context = {'formulario':formulario}
    return render(request,'administracion/edificios/nuevo.html',context)

@login_required
@staff_member_required
def edificios_editar(request,id_edificio):
    try:
        edificio = Edificio.objects.get(pk=id_edificio)
    except Edificio.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = EdificioForm(request.POST, instance=edificio)
        if formulario.is_valid():
            formulario.save()
            return redirect('edificios_index')
    else:
        formulario = EdificioForm(instance=edificio)
    return render(request,'administracion/edificios/editar.html',{'formulario':formulario})

@login_required
@staff_member_required
def edificios_eliminar(request,id_edificio):
    try:
        edificio = Edificio.objects.get(pk=id_edificio)
    except Edificio.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    edificio.delete()
    return redirect('edificios_index')

@login_required
@staff_member_required
def unidad_funcional_index(request):
    unidad_funcional = UnidadFuncional.objects.all()
    return render(request,'administracion/unidades/index.html',{'unidades_funcionales':unidad_funcional})

@login_required
@staff_member_required
def unidad_funcional_nuevo(request):
    if request.method =='POST':
        formulario = UnidadFuncionalForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('../unidades')
        else:
            messages.error(request,("Revise el formulario"))
    else:
        formulario = UnidadFuncionalForm()

    context = {'formulario':formulario}
    return render(request,'administracion/unidades/nuevo.html',context)

@login_required
@staff_member_required
def unidad_funcional_editar(request,id_unidad):
    try:
        unidad_funcional = UnidadFuncional.objects.get(pk=id_unidad)
    except UnidadFuncional.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = UnidadFuncionalForm(request.POST, instance=unidad_funcional)
        if formulario.is_valid():
            formulario.save()
            return redirect('unidades_index')
    else:
        formulario = UnidadFuncionalForm(instance=unidad_funcional)
    return render(request,'administracion/unidades/editar.html',{'formulario':formulario})

@login_required
@staff_member_required
def unidad_funcional_eliminar(request,id_unidad):
    try:
        unidad_funcional = UnidadFuncional.objects.get(pk=id_unidad)
    except Edificio.DoesNotExist:
        return render(request,'administracion/404_admin.html')
    unidad_funcional.delete()
    return redirect('unidades_index')

@login_required
@staff_member_required
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request,'administracion/reservas.html',{'reservas':reservas})

@login_required
@staff_member_required
def reclamos(request):
    reclamos = ReclamoSugerencia.objects.all()
    return render(request,'administracion/reclamos.html',{'reclamos':reclamos})