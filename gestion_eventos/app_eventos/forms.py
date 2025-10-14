from django import forms
from .models import Eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['nombre', 'descripcion', 'lugar', 'fecha', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del evento'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del evento',
                'rows': 4
            }),
            'lugar': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Lugar del evento',
                'rows': 2
            }),
            'fecha': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'lugar': 'Lugar',
            'fecha': 'Fecha y Hora',
            'imagen': 'Imagen'
        }