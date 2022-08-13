from django.shortcuts import render
from apps.modelo.models import Avion,Cliente, Asiento
from .forms import FormularioAvion
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "avion").exists() or usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaAvion = Avion.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaAvion = Avion.objects.filter(
                Q(numero__icontains = busqueda) |
                Q(aereolinea__icontains = busqueda) 
            ).distinct() 
        return render (request, 'aviones/index_Todos.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

@login_required
def crearAvion(request):
    usuario = request.user
    if usuario.groups.filter(name = "avion").exists() or usuario.groups.filter(name = "gestion_aereopuerto").exists():
        formulario_avion = FormularioAvion(request.POST)
        if request.method == 'POST':
            if formulario_avion.is_valid():

                avion = Avion()
                datos_avion = formulario_avion.cleaned_data
                avion.numero = datos_avion.get('numero')
                avion.capacidad= datos_avion.get('capacidad')
                avion.puestos_Disponibles= avion.capacidad
                avion.aereolinea = datos_avion.get('aereolinea')
                #ORM
                cant = avion.puestos_Disponibles
                avion.save()
                i=1
                while i <= cant:
                    asiento = Asiento()
                    asiento.numero=i
                    asiento.avion=avion
                    if i % 3 == 1:
                        asiento.categoria='ventana'
                    elif i % 3 == 2:
                        asiento.categoria='medio'
                    else:
                        asiento.categoria='pasillo'
                    asiento.save()
                    i +=1

            return redirect(index)
        return render (request, 'aviones/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

def eliminarAvion(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "avion").exists() or usuario.groups.filter(name = "gestion_aereopuerto").exists():
        avion = Avion.objects.get(numero=numero)
        avion.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())
