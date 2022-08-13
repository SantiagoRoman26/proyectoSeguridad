from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='aereolineas'),
    path('crearAereolinea', views.crearAereolinea, name='crear_aereolinea'),
    path('eliminarAereolinea/<int:numero>/', views.eliminarAereolinea, name='eliminar_aereolinea'),
     path('modificarAereolinea/<int:numero>/', views.modificarAereolinea, name='modificar_aereolinea'),
]