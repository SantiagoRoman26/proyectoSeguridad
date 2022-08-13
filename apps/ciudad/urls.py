from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ciudades'),
    path('crearCiudad', views.crearCiudad, name='crear_ciudad'),
    path('eliminarCiudad/<int:numero>/', views.eliminarCiudad, name='eliminar_ciudad'),
     path('modificarCiudad/<int:numero>/', views.modificarCiudad, name='modificar_ciudad'),
]