from django import forms
from .models import Mascotas,Usuario

class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = [
            'nombres',
            'edad',
            'genero',
            'animal',
            'descripcion',
            'imagen',
        ]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'correo',
            'edad',
            'telefono',
        ]