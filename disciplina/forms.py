from django import forms
from django.db.models import Q
from django.forms import ModelForm
from disciplina.models import Disciplina



class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'codigo', 'sigla']
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        