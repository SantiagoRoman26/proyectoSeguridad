from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FormularioLogin, FormularioRegistrar, CambiarPassword
from django.contrib.auth.models import Group, User
from apps.modelo.models import Cliente
from django.contrib import messages
from BruteBuster.models import FailedAttempt
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def autenticar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username = usuario, password=clave)
            if FailedAttempt.objects.filter(username = usuario).exists():
                control=FailedAttempt.objects.get(username=usuario) 
                numFallos=control.failures
            else:
                numFallos = 0
            if numFallos < 5:
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('homepage'))
                    else:
                        
                        return HttpResponseRedirect(reverse('no_activo'))
                else:
                    messages.add_message(request, messages.INFO, 'Usuario o Clave incorrectas')
            else:
                messages.add_message(request, messages.INFO, 'Demasiados intentos fallidos. Cuenta bloqueada')
        

    else:    
        formulario = FormularioLogin()
    context = {
        'formulario': formulario
    }
    return render (request, 'login/login.html', context) 

def desautenticar(request):
    logout(request)
    return render (request, 'login/logout.html')

def registrar (request):
    if request.method == 'POST':
        formulario = FormularioRegistrar(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']    
            correo = request.POST['email']
            nombres = request.POST['first_name']
            apellidos = request.POST['last_name']
            if User.objects.filter(username=usuario).exists():
                messages.add_message(request, messages.INFO, 'Username is already in use.')
                return redirect(registrar)
            else:
                if User.objects.filter(email=correo).exists():
                    messages.add_message(request, messages.INFO, 'email is already in use.')
                    return redirect(registrar)
                user = User.objects.create_user(usuario,correo,clave)
                user.last_name=apellidos
                user.first_name=nombres
                cliente=Group.objects.get(name='cliente')
                user.groups.add(cliente)
                user.save()

                cliente = Cliente()
                cliente.apellidos=apellidos
                cliente.nombres=nombres
                cliente.correo=correo
                cliente.cedula = user.id
                cliente.save()
        else:
            messages.error(request, 'Registration Failed')
            return redirect(registrar)
        return redirect(autenticar)
    else:    
        formulario = FormularioRegistrar()
        
    context = {
        'formulario': formulario
    }
    return render(request, 'login/registrar.html', context)  

def passwordChange(request):
    if request.method == 'POST':
        formulario = PasswordChangeForm(request.user, request.POST)
        if formulario.is_valid():
            user = formulario.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('homepage'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        formulario = PasswordChangeForm(request.user)

    context = {
        'formulario': formulario
    }
    return render(request, 'login/passwordChange.html', context)    

def welcome (request):
    return (request, 'login/welcome.html')

def forbidden (request):
    return (request, 'login/forbidden.html') 

def desactivado (request):
    return render(request, 'login/deactive.html')  

