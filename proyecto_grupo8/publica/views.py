from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "publica/index.html")

def reservas(request):
    parameters = ("Usuario","Reserva 1")
    return render(request, "publica/reservas.html", {"parameters": parameters})
