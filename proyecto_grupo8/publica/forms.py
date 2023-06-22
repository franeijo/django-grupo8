import datetime
from django import forms
from administracion.models import ReclamoSugerencia
    
class ReclamoForm(forms.ModelForm):
    class Meta:
        model=ReclamoSugerencia
        fields=['fecha','tipo','asunto','descripcion','usuario']

        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'tipo' : forms.Select(attrs={'class':'form-select'}),
            'asunto' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el asunto'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una descripcion'}),
            'usuario': forms.Select(attrs={'class':'form-select'})
        }

        labels = {
            "usuario": ""
        }
        