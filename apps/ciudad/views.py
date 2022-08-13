from django.shortcuts import render
from apps.modelo.models import Ciudad
from .forms import FormularioCiudad
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaCiudad = Ciudad.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaCiudad = Ciudad.objects.filter(
                Q(nombre__icontains = busqueda) | 
                Q(pais__icontains = busqueda) 
            ).distinct() 
        return render (request, 'ciudades/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

@login_required
def crearCiudad(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        formulario_ciudad = FormularioCiudad(request.POST)
        if request.method == 'POST':
            if formulario_ciudad.is_valid():

                ciudad = Ciudad()
                datos_ciudad = formulario_ciudad.cleaned_data
                ciudad.nombre = datos_ciudad.get('nombre')
                ciudad.nombreAereopuerto = datos_ciudad.get('nombreAereopuerto')
                ciudad.pais = datos_ciudad.get('pais')
                #ORM
                ciudad.save()
            return redirect(index)
        return render (request, 'ciudades/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

def eliminarCiudad(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        ciudad = Ciudad.objects.get(ciudad_id=numero)
        ciudad.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

def modificarCiudad(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        ciudad = Ciudad.objects.get(ciudad_id=numero)
        if request.method == 'GET':
            formulario_ciudad = FormularioCiudad(instance = ciudad)
        else:
            formulario_ciudad = FormularioCiudad(request.POST, instance = ciudad)
            if formulario_ciudad.is_valid():
                #ORM
                formulario_ciudad.save()
            return redirect(index)
        return render (request, 'ciudades/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())