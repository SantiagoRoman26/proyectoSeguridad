from django import forms
from apps.modelo.models import Cliente, Avion,Viaje
class FormularioAvion(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ["numero","capacidad","aereolinea"]