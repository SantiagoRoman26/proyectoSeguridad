from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='asientos'),
    #path('crearCliente', views.crearCliente, name='crear_cliente'),
    #path('eliminarCliente/<int:cedula>/', views.eliminarCliente, name='eliminar_cliente'),
    #path('modificarCliente/<int:cedula>/', views.modificarCliente, name='modificar_cliente'),
    #path('actualizarCliente', views.actualizarCliente, name="actualizar_cliente")
    
]