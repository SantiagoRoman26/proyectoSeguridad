from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='paises'),
    path('crearPais', views.crearPais, name='crear_pais'),
    path('eliminarPais/<int:numero>/', views.eliminarPais, name='eliminar_pais'),
     path('modificarPais/<int:numero>/', views.modificarPais, name='modificar_pais'),
]