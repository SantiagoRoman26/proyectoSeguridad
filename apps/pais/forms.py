from django import forms
from apps.modelo.models import Pais
class FormularioPais(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ["nombre"]