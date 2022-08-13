from django import forms
from apps.modelo.models import Ciudad
class FormularioCiudad(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["nombre","nombreAereopuerto","pais"]