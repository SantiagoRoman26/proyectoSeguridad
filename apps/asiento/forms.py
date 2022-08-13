from django import forms
from apps.modelo.models import Asiento
class FormularioAsiento(forms.ModelForm):
    class Meta:
        model = Asiento
        fields = ["numero","categoria","avion"]