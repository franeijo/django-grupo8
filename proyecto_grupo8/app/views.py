from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def reservas(request):
    parameters = ("Usuario","Reserva 1")
    return render(request, "reservas.html", {"parameters": parameters})