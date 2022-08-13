from django.shortcuts import render
from apps.modelo.models import Pais
from .forms import FormularioPais
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaPais = Pais.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaPais = Pais.objects.filter(
                Q(nombre__icontains = busqueda)  
            ).distinct() 
        return render (request, 'paises/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

@login_required
def crearPais(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        formulario_pais = FormularioPais(request.POST)
        if request.method == 'POST':
            if formulario_pais.is_valid():

                pais = Pais()
                datos_pais = formulario_pais.cleaned_data
                pais.nombre = datos_pais.get('nombre')
                #ORM
                pais.save()
            return redirect(index)
        return render (request, 'paises/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

def eliminarPais(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        pais = Pais.objects.get(pais_id=numero)
        pais.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

def modificarPais(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        pais = Pais.objects.get(pais_id=numero)
        if request.method == 'GET':
            formulario_pais = FormularioPais(instance = pais)
        else:
            formulario_pais = FormularioPais(request.POST, instance = pais)
            if formulario_pais.is_valid():
                #ORM
                formulario_pais.save()
            return redirect(index)
        return render (request, 'paises/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
