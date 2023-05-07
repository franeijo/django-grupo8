from django import forms
from django.forms import ValidationError
import re

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

def validate_phone(value):
    phone_regex =r'^(\+\d{1,3})?,?\s?\d{8,13}'
    if not re.match(phone_regex,value):
        raise ValidationError('Telefono inválido')
    return value

class ReclamoForm(forms.Form):
    
    nombreUsuario = forms.CharField(
        label='Nombre',
        max_length=100,
        validators=(solo_caracteres,),
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.TextInput(
            attrs={'class':"form-control form-control-sm"}
        ),
    )
    apellidoUsuario = forms.CharField(
        label='Apellido',
        max_length=100,
        validators=(solo_caracteres,),
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.TextInput(
            attrs={'class':'form-control form-control-sm'}
        ),
    )
    PROBLEMAS_POSIBLES = (
        ('PG',"Acreditación de transferencias"),
        ('CA',"Uso compartido de ammenities"),
        ('LE',"Limpieza de Espacios comunes"),
        ('IF',"Infestaciones/Plagas"),
        ('PS',"Problemas con los servicios"),
        ('RM',"Ruidos y Molestias"),
        ('IS',"Inseguridad"),
        ('OT',"Otros (aclarar)"),
    )
    problemasOpciones = forms.ChoiceField(
        label='Tengo un problema con...',
        choices=PROBLEMAS_POSIBLES,
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.Select(attrs={'class':'form-select form-select-sm'})

    )
    EDIFICIOS_HABILITADOS = (
        ('SB',"Sanchez de Bustamante 364"),
        ('BY','Boyacá 372'),
        ('AC','Acuña de Figueroa 1570'),
    )
    locacionEdificio = forms.ChoiceField(
        label="Estoy en...",
        choices=EDIFICIOS_HABILITADOS,
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.Select(attrs={'class':'form-select form-select-sm'}),
    )
    problemasTexto = forms.CharField(
        label="detallanos tu problema:",
        widget=forms.Textarea(attrs={"rows":10,"cols":50}),
        max_length=500,
        )
    contactoUsuario = forms.CharField(
        label="numero de telefono:",
        validators=(validate_phone,),
        error_messages={
            'required':'Por favor completa el campo'
        },
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'tel','placeholder':'+1111111111'})
        )
    emailUsuario = forms.EmailField(
        label='Email',
        max_length=100, 
        validators=(validate_email,),
        error_messages={
            'required': 'Por favor completa el campo'
        },
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','type':'email','placeholder':'email@dominio.com'}),
    )