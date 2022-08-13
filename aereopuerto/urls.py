"""aereopuerto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aereolinea/', include('apps.aereolinea.urls')),
    path('asiento/', include('apps.asiento.urls')),
    path('aviones/', include('apps.avion.urls')),
    path('boleto/', include('apps.boleto.urls')),
    path('ciudad/', include('apps.ciudad.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('aereopuerto/', include('apps.gestion_aereopuerto.urls')),
    path('pais/', include('apps.pais.urls')),
    
    path('login/', include('apps.login.urls')),
    

    path('about/', views.about, name='about'),
    path('', views.index, name='homepage')
]

handler404='aereopuerto.views.handle_not_found'