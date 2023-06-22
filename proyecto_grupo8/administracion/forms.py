from django import forms

from .models import Edificio, UnidadFuncional
from django.contrib.auth.models import User


class EdificioForm(forms.ModelForm):
    class Meta:
        model=Edificio
        fields='__all__'

        widgets = {
            'provincia' : forms.Select(attrs={'class':'form-select'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una ciudad'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese una direccion'}),
        }
        

class UnidadFuncionalForm(forms.ModelForm):

    edificio = forms.ModelChoiceField(
        label='Edificio',
        queryset=Edificio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    usuario = forms.ModelChoiceField(
        label='Usuario',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model=UnidadFuncional
        fields=['unidad_funcional','piso','dpto','edificio','usuario']
        widgets = {
            'unidad_funcional' : forms.TextInput(attrs={'class':'form-control'}),
            'piso' : forms.TextInput(attrs={'class':'form-control'}),
            'dpto' : forms.TextInput(attrs={'class':'form-control'}),
        }