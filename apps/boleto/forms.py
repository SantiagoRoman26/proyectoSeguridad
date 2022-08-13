from django import forms
from apps.modelo.models import Boleto
class FormularioBoleto(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ["cliente","viaje","num_asiento","categoria_asiento","coste"]