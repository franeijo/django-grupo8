from django import forms
from django.forms import ValidationError
import re

from .models import Edificio

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value
 
class NuevoUsuario(forms.Form):
    
    nombre = forms.CharField(
            label='Nombre', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control form-control-sm'}
                    )
    )
    apellido = forms.CharField(
            label='Apellido', 
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(
                    attrs={'class':'form-control form-control-sm'}
                    )
    )
    email = forms.EmailField(
            label='Email',
            max_length=100, 
            validators=(validate_email,),
            error_messages={
                    'required': 'Por favor completa el campo'
                },
            widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'email','placeholder':'email@dominio.com'})
        )
    SEXO_LISTADO = (
        ('','Seleccione'),
        (1,'Masculino'),
        (2,'Femenino'),
        (3,'X'),
    )
    sexo = forms.ChoiceField(
        label='Sexo',
        choices=SEXO_LISTADO,
        error_messages={
                    'required': 'Por favor completa el campo'
                },
        widget=forms.Select(attrs={'class':'form-select form-select-sm'})
    )


class EdificioForm(forms.ModelForm):
    class Meta:
        model=Edificio
        fields='__all__'

        widgets = {
            'provincia' : forms.Select(attrs={'class':'form-select'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una ciudad'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una direccion'}),
        }