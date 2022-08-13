from django.shortcuts import render
from apps.modelo.models import Viaje,Avion,Cliente,Asiento,Boleto
from .forms import FormularioViaje
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
from django import template
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "cliente").exists():
        cliente = Cliente.objects.get(correo=usuario.email)
        listaBoletos = Boleto.objects.filter(cliente=cliente) 
    listaViajes = Viaje.objects.all()
    
    busqueda = request.POST.get("busqueda")
    if busqueda:
        listaViajes = Viaje.objects.filter(
            Q(numero__icontains = busqueda) | 
            Q(destino__icontains = busqueda) 
        ).distinct() 
    return render (request, 'viajes/index.html', locals())


@login_required
def crearViaje(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        formulario_viaje = FormularioViaje(request.POST)
        if request.method == 'POST':
            if formulario_viaje.is_valid():

                viaje = Viaje()
                datos_viaje = formulario_viaje.cleaned_data
                viaje.numero = datos_viaje.get('numero')
                viaje.destino= datos_viaje.get('destino')
                viaje.fechaViaje= datos_viaje.get('fechaViaje')
                viaje.fechaLlegada= datos_viaje.get('fechaLlegada')
                viaje.avion=datos_viaje.get('avion')
                #ORM
                viaje.save()
            return redirect(index)
        return render (request, 'viajes/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
@login_required
def modificarViaje(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        viaje = Viaje.objects.get(numero=numero)
        if request.method == 'GET':
            formulario_viaje = FormularioViaje(instance = viaje)
        else:
            formulario_viaje = FormularioViaje(request.POST, instance = viaje)
            if formulario_viaje.is_valid():
                #ORM
                formulario_viaje.save()
            return redirect(index)
        return render (request, 'viajes/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
@login_required    
def eliminarViaje(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        viaje = Viaje.objects.get(numero=numero)
        viaje.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())
@login_required
def listarAviones(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists() or usuario.groups.filter(name = "avion").exists():
        viaje = Viaje.objects.get(numero=numero)
        avion = Avion.objects.filter(viaje=viaje)
        cliente = Cliente.objects.get(correo=usuario.email)
        

        return render(request, 'aviones/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())
# CLiente puede selecionar un viaje, seguidamente su asiento y actualizara sus datos.
@login_required
def solicitarViaje(request,numero):
    usuario = request.user
    if usuario.groups.filter(name = "cliente").exists():
        cliente = Cliente.objects.get(correo=usuario.email)
        viaje = Viaje.objects.get(numero=numero)
        avion= viaje.avion   
        #cliente.avion = viaje.avion                    
        
        if avion.puestos_Disponibles==0:
                return redirect(index) #sin puestos disponibles.html 
        else:
            avion.puestos_Disponibles=avion.puestos_Disponibles-1
            if avion.puestos_Disponibles==0:
                avion.estado=False
                #ORM
        cliente.save()    
        avion.save()
        boleto = Boleto()
        boleto.cliente = cliente
        boleto.viaje = viaje
        boleto.save()    
        listaAsiento = Asiento.objects.filter(avion=avion)
        return redirect(listarAsientos, numero)             #ummmmm
        #return render(request, 'asiento/index.html', locals())
            
    else:
        return render(request, 'login/forbidden.html', locals())

    #       asientos del viaje para la generacion del boleto
@login_required
def listarAsientos(request, numero):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists() or usuario.groups.filter(name = "cliente").exists():
        viaje = Viaje.objects.get(numero=numero)
        avion = viaje.avion
        listaAsiento = Asiento.objects.filter(avion=avion)
        
        return render(request, 'asiento/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

@login_required
def seleccionarAsiento(request,numeroAsiento, numeroViaje):
    usuario = request.user
    if usuario.groups.filter(name = "cliente").exists():
        cliente = Cliente.objects.get(correo=usuario.email)
        viaje = Viaje.objects.get(numero=numeroViaje)
        avion = viaje.avion
        asiento = Asiento.objects.filter(avion=avion).get(numero=numeroAsiento)
        
        asiento.estado=False
        asiento.save()
        boletos = Boleto.objects.filter(cliente=cliente)
        boleto = boletos.get(viaje=viaje)        #ummmmm boleto=Boleto.objects.filter(cliente=cliente).get(viaje.viaje)
        boleto.num_asiento = asiento.numero
        boleto.categoria_asiento = asiento.categoria
        boleto.save()
        return HttpResponseRedirect(reverse('actualizar_cliente'))
        
    else:
        return render(request, 'login/forbidden.html', locals())

def listarClientes(request, numero): #ummm (correcto)
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        viaje = Viaje.objects.get(numero=numero)
        #avion = Avion.objects.get(numero=numero) #boleto
        boletos = Boleto.objects.filter(viaje=viaje)
    return render(request, 'clientes/index.html', locals())