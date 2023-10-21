from django import forms
from django.forms import ValidationError
from administracion.models import Categoria, Curso, Estudiante, Comision, Docente, Proyecto, Inscripcion


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Error1',
                              params={'valor': value})


# class CategoriaForm(forms.Form):
#     nombre = forms.CharField(
#         label='Nombre:',
#         required=True,
#         validators=(solo_caracteres,),
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto'})
#     )

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre:',
        required=True,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto 1'})
    )

    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese solo texto 2 '})
        }


class CursoForm(forms.ModelForm):

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha_inicio = forms.DateField(
        label='Fecha Inicio',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    """Se utiliza ModelChoiceField para poder realizar un filtrado de lo que
    quiero mostrar en el selector"""
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    portada = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Curso
        fields = ['nombre', 'fecha_inicio', 'portada', 'descripcion', 'categoria']

class EstudianteForm(forms.ModelForm):

    class Meta:
        model=Estudiante
        fields=['nombre','apellido','email','dni','matricula']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'matricula': forms.TextInput(attrs={'class':'form-control'}),
        }

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = ("nombre", "apellido",'email','dni','legajo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'legajo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProyectoForm(forms.ModelForm):

    class Meta:
        model=Proyecto
        fields=['nombre','descripcion','anio','url','portada','estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5,'class':'form-control'}),
            'anio': forms.NumberInput(attrs={'class':'form-control'}),
            'url': forms.URLInput(attrs={'class':'form-control'}),
            'portada': forms.FileInput(attrs={'class':'form-control'}),
            'estudiante': forms.Select(attrs={'class':'form-control'}),
        }

# Formularios asociados a modelos
class InscripcionForm(forms.ModelForm):
    
    comision = forms.ModelChoiceField(
        queryset=Comision.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.filter(baja=False),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=Inscripcion.Estado.choices,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    class Meta:
        model=Inscripcion
        fields=['comision','estudiante','estado']
        

class ComisionForm(forms.ModelForm):

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    horario = forms.CharField(
        label='Horario',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    link_meet = forms.URLField(
        label='Link de meet',
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
    )
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Comision
        fields = ['nombre', 'horario','link_meet', 'descripcion', 'curso']
