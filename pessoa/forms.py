from django import forms
from django.db.models import Q
from django.forms import ModelForm
from pessoa.models import Pessoa
from configuracao.models import Documento_identificacao



class Pessoa_Form(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    nome_pai = forms.CharField(max_length=100, required=False,  widget=forms.TextInput(attrs={'class': 'form-control '}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class': 'form-control '}))
    ndi = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control '}))
    residencia = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))
    municipio = forms.CharField(max_length=60,required=False,  widget=forms.Select(choices="", attrs={'class': 'form-control'}))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae','genero','data_nascimento', 'estado_civil', 'residencia', 'provincia', 'telefone','documento', 'email', 'nacionalidade']

        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control '}),
            'genero': forms.Select( attrs={'class': 'form-control'}),
            'estado_civil': forms.Select( attrs={'class': 'form-control'}),
            'documento': forms.Select( attrs={'class': 'form-control'}),
            'nacionalidade': forms.Select( attrs={'class': 'form-control '}),
            'data_nascimento': forms.DateInput( attrs={'class': 'form-control'}),
        }
