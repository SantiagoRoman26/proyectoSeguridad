from django import forms
from apps.modelo.models import Cliente, Avion,Viaje

class FormularioViaje(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ["numero","destino","fechaViaje","fechaLlegada","avion"]


