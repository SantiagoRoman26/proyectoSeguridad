from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='boletos'),
    path('listarBoletos', views.listarBoletos, name='listar_boletos'),
    #path('eliminarCliente/<int:cedula>/', views.eliminarCliente, name='eliminar_cliente'),
    #path('modificarCliente/<int:cedula>/', views.modificarCliente, name='modificar_cliente'),
    #path('actualizarCliente', views.actualizarCliente, name="actualizar_cliente")
    
]