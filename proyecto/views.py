from django.shortcuts import render
from django.http import HttpResponse

# Cerastes esta vista aquí.
def inicio(requests):
    return HttpResponse("La rata hambrienta quiere un trozo de queso.")
