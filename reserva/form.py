from dataclasses import fields
from django import forms
from .models import Reserva

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        
