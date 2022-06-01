import datetime
from django import forms
from django.forms import ModelForm
from app_jugadores.forms import *


class JugadoresForm(forms.Form):
    nombre = forms.CharField(max_length=40, min_length=3, label='Nombre')
    equipo = forms.CharField(max_length=30, min_length=3, label='Equipo')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimieto', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))


class ClubForm(forms.Form):
    nombre = forms.CharField(max_length=30, min_length=3, label='Nombre')
    provincia = forms.CharField(max_length=30, min_length=3, label='Provincia')
    localidad = forms.CharField(max_length=30, min_length=3, label='Localidad')

class LigaForm(forms.Form):
    torneo = forms.CharField(max_length=40, min_length=3, label='Torneo')
    equipos = forms.IntegerField(label='Equipos')
    internacional = forms.BooleanField(label='Internacional', required=False)

# class ProfesorForm(ModelForm):
#     class Meta:
#         model = Profesor
#         fields = '__all__'
