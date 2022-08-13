from django.shortcuts import render
from apps.modelo.models import Asiento, Avion
from .forms import FormularioAsiento
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
        listaAsientos = Asiento.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaClientes = Cliente.objects.filter(
                Q(numero__icontains = busqueda) | 
                Q(categoria__icontains = busqueda) | 
                Q(avion__icontains = busqueda) 
            ).distinct() 
        return render (request, 'asiento/index_Todos.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals())