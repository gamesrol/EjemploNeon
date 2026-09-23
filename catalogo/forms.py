from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Autor, Categoria, Libro

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=False, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email']


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'anio', 'categorias']
        widgets = {
            'categorias': forms.SelectMultiple,
        }