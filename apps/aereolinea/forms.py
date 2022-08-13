from django import forms
from apps.modelo.models import Aereolinea
class FormularioAereolinea(forms.ModelForm):
    class Meta:
        model = Aereolinea
        fields = ["nombre"]