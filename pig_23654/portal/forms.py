import re
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class ContactoForm(forms.Form):
#     nombre = forms.CharField(label="Nombre:", max_length=20, required=False)
#     consulta = forms.CharField(label="Alguna consulta?:", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(label="Consulta?:")
#     edad = forms.IntegerField(label="TuEdad:", min_value=1, max_value=90)


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Invalid',
                              params={'valor': value})


def custom_validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')


class ContactoForm(forms.Form):
    TIPO_CONSULTA = (
        ('', '-Seleccione-'),
        (1, 'Inscripciones'),
        (2, 'Soporte Aula Virtual'),
        (3, 'Ser instructor/a'),
    )
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Solo letras'}
        )
    )

    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        # validators=(custom_validate_email,),
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'})
        # widget=forms.TextInput(
        #     attrs={'class': 'form-control', 'type': 'email'})
    )
    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        label='Mensaje',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las novedades de codo a codo',
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input', 'value': 1})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError(
                "Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and nombre and ("HOMERO" in nombre.upper()):
            msg = "No le brindamos información a Homeros."
            self.add_error('nombre', msg)
            raise ValidationError(msg)
        
class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

