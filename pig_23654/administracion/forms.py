from django import forms
from django.forms import ValidationError


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})


class CategoriaForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre:',
        required=True,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto'})
    )
