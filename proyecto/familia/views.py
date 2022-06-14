from contextvars import Context
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from familia.models import familiar
from django.template import Template, Context
from django.template import loader

# Create your views here.


def familiar1(self):
    name="Roberto Escobar"
    year=21
    born="2000-07-04"
    height=1.75
    fami1 = familiar(nombre=name,
    edad=year,
    nacimiento=born,
    altura=height)
    fami1.save()

    diccionario = {"nombre":name,"edad":year,"nacimiento":born,"altura":height}
    
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def familiar2(self):
    nom2="Ramiro Escobar"
    edad2=32
    naci2="1990-12-26"
    alt2=1.92
    fami1 = familiar(nombre=nom2,
    edad=edad2,
    nacimiento=naci2,
    altura=alt2)
    fami1.save()
    diccionario = {"nombre":nom2,"edad":edad2,"nacimiento":naci2,"altura":alt2}

    plantilla = loader.get_template("template2.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def familiar3(self):
    nom3="Martina Escobar"
    edad3=15
    naci3="2007-01-15"
    alt3=1.65
    fami1 = familiar(nombre=nom3,
    edad=edad3,
    nacimiento=naci3,
    altura=alt3)
    fami1.save()

    diccionario = {"nombre":nom3,"edad":edad3,"nacimiento":naci3,"altura":alt3}
    
    plantilla = loader.get_template("template3.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
