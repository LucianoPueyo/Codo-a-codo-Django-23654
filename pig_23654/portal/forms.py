from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=20, required=False)
    consulta = forms.CharField(label="Alguna consulta?:", required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Consulta?:")
    edad = forms.IntegerField(label="TuEdad:", min_value=1, max_value=90)
