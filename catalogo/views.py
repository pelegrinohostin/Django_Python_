from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lista_videojuegos(request):
    return HttpResponse("Bienvenidos a la Lista de videojuegos! 🎮")
   
