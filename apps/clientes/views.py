from django.shortcuts import render
from apps.modelo.models import Cliente, Boleto, Asiento
from .forms import FormularioCliente
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaClientes = Cliente.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaClientes = Cliente.objects.filter(
                Q(cedula__icontains = busqueda) | 
                Q(apellidos__icontains = busqueda) | 
                Q(nombres__icontains = busqueda) 
            ).distinct() 
        return render (request, 'clientes/index_Todos.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 


@login_required
def crearCliente(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto" ).exists() and usuario.has_perm('cliente.add_cliente'):
        formulario_cliente = FormularioCliente(request.POST)
        if request.method == 'POST':
            if formulario_cliente.is_valid():
                cliente = Cliente()
                datos_cliente = formulario_cliente.cleaned_data
                cliente.cedula = datos_cliente.get('cedula')
                cliente.apellidos= datos_cliente.get('apellidos')
                cliente.nombres= datos_cliente.get('nombres')
                cliente.genero= datos_cliente.get('genero')
                cliente.correo= datos_cliente.get('correo')
                cliente.celular= datos_cliente.get('celular')
                
                    #ORM
            
                cliente.save()
            
            return redirect(index)
        return render (request, 'clientes/crear.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

def eliminarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        cliente = Cliente.objects.get(cedula=cedula)
        #avion=cliente.avion                         #boleto
        listaBoletos = Boleto.objects.filter(cliente=cliente)
        for boleto in listaBoeltos:
            viaje = boleto.viaje
            if(viaje.estado == True):
                avion=viaje.avion
                if avion.estado==False:
                    avion.estado=True
            avion.puestos_Disponibles=avion.puestos_Disponibles+1
            listaAsientos = Asiento.objects.filter(avion=avion)
            for asientos in listaAsientos:
                asiento = asientos.objects.get(numero=boleto.num_asiento)
                asiento.estado= True
                asiento.save()
            avion.save()
        cliente.delete()
        return redirect(index)
    else:
        return render(request, 'login/forbidden.html', locals())

def modificarCliente(request, cedula):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        cliente = Cliente.objects.get(cedula=cedula)
        if request.method == 'GET':
            formulario_cliente = FormularioCliente(instance = cliente)
        else:
            formulario_cliente = FormularioCliente(request.POST, instance = cliente)
            if formulario_cliente.is_valid():
                #ORM
                formulario_cliente.save()
            return redirect(index)
        return render (request, 'clientes/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())

def actualizarCliente(request):
    usuario = request.user
    if usuario.groups.filter(name = "cliente").exists():
        correo = usuario.email
        cliente = Cliente.objects.get(correo=correo)
        if request.method == 'GET':
            formulario_cliente = FormularioCliente(instance = cliente)
        else:
            formulario_cliente = FormularioCliente(request.POST, instance = cliente)
            if formulario_cliente.is_valid():
                #ORM
                formulario_cliente.save()
            return HttpResponseRedirect(reverse('viajes'))
        return render (request, 'clientes/modificar.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())