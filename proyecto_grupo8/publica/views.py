from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from publica.reclamos import ReclamoForm
def index(request):
    return render(request, "publica/index.html")

def reservas(request):
    parameters = ("Usuario","Reserva 1")
    return render(request, "publica/reservas.html", {"parameters": parameters})

def reclamos(request):
    user = ("Alejandro","Unidad 1")
    if request.method == 'POST':
        #create a form instance and populate it with data from the request:
        form = ReclamoForm(request.POST)
        if form.is_valid():
            #arre que no se que hacer acá
            return HttpResponseRedirect('/thanks/')
    else:
        form = ReclamoForm()
    return render(request,"publica/reclamos.html",{"user":user,"form":form})