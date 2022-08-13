from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='viajes'),
    path('crearViaje', views.crearViaje, name='crear_viaje'),
    path('modificarViaje/<int:numero>/', views.modificarViaje, name='modificar_viaje'),
    path('eliminarViaje/<int:numero>/', views.eliminarViaje, name='eliminar_viaje'),
    path('avions/<int:numero>/', views.listarAviones, name="avions"),
    path('listaAsientos/<int:numero>/', views.listarAsientos, name="lista_asientos"),
    path('seleccionarAsiento/<int:numeroAsiento>/<int:numeroViaje>/', views.seleccionarAsiento, name='seleccionar_asiento'),
    path('solicitarViaje/<int:numero>/', views.solicitarViaje, name='solicitar_viaje'),
    path('clientes/<int:numero>/', views.listarClientes, name="clientes"),
]