from django import forms
from .models import Vehiculo

class formulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('autor','vin','patente','año_fabricacion','fecha_recepcion','marca','modelo',)