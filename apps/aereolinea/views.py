from django.shortcuts import render
from apps.modelo.models import Aereolinea
from .forms import FormularioAereolinea
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

def index(request):
    usuario = request.user
    listaAereolinea = Aereolinea.objects.all() 
    busqueda = request.POST.get("busqueda")
    if busqueda:
        listaAereolinea = Aereolinea.objects.filter(
            Q(nombre__icontains = busqueda)  
        ).distinct() 
    return render (request, 'aereolineas/index.html', locals())
 

@login_required
def crearAereolinea(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        formulario_aereolinea = FormularioAereolinea(request.POST)
        if request.method == 'POST':
            if formulario_aereolinea.is_valid():

                aereolinea = Aereolinea()
                datos_aereolinea = formulario_aereolinea.cleaned_data
                aereolinea.nombre = datos_aereolinea.get('nombre')
                #ORM
                aereolinea.save()
            return redirect(index)
        return render (request, 'aereolineas/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

def eliminarAereolinea(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        aereolinea = Aereolinea.objects.get(aereolinea_id=numero)
        aereolinea.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

def modificarAereolinea(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        aereolinea = Aereolinea.objects.get(aereolinea_id=numero)
        if request.method == 'GET':
            formulario_aereolinea = FormularioAereolinea(instance = aereolinea)
        else:
            formulario_aereolinea = FormularioAereolinea(request.POST, instance = aereolinea)
            if formulario_aereolinea.is_valid():
                #ORM
                formulario_aereolinea.save()
            return redirect(index)
        return render (request, 'aereolineas/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())