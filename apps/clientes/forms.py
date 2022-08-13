from django import forms
from apps.modelo.models import Cliente, Avion,Viaje
class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula","apellidos","nombres","genero","correo","celular"]