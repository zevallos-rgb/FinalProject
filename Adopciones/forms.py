from django import forms
from .models import Mascotas
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