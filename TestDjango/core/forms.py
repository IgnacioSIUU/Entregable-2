from django import forms
from django.forms import ModelForm
from .models import Arte

class ArteForm(ModelForm):
    class Meta:
        model = Arte
        fields = ['idprod','nombre','precio','categoria']
        
