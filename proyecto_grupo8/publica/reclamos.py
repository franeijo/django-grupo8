from django import forms
from django.core.validators import RegexValidator

class ReclamoForm(forms.Form):
    PROBLEMAS_POSIBLES = [
    ('PG',"Acreditación de transferencias"),
    ('CA',"Uso compartido de ammenities"),
    ('LE',"Limpieza de Espacios comunes"),
    ('IF',"Infestaciones/Plagas"),
    ('PS',"Problemas con los servicios"),
    ('RM',"Ruidos y Molestias"),
    ('IS',"Inseguridad"),
    ('OT',"Otros (aclarar)")
    ]
    nombreUsuario = forms.CharField(widget=forms.TextInput(attrs={"class":"special"}),label='Nombre',max_length=100, initial="Tu nombre")
    apellidoUsuario = forms.CharField(label='Apellido',max_length=100, initial="Tu apellido")
    problemasOpciones = forms.ChoiceField(choices=PROBLEMAS_POSIBLES,label='Tengo un problema con...')
    locacionEdificio = forms.CharField(label="Estoy en...", initial="tu domicilio", max_length=100)
    problemasTexto = forms.CharField(label="detallanos tu problema:",widget=forms.Textarea(attrs={"rows":7,"cols":25}),max_length=500)
    contactoUsuario = forms.CharField(label="numero de telefono:",validators=[RegexValidator(r"^[0-9]+$", "Por favor ingresa un numero de telefono."),])
    emailUsuario = forms.EmailField(label="Email de contacto:", max_length=100)