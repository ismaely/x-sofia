from django import forms
from django.db.models import Q
from django.forms import ModelForm
from pessoa.models import Pessoa
from configuracao.models import Curso, Periodo
from aluno.models import Aluno, Inscricao


class Inscricao_Form(ModelForm):
    #grau = forms.CharField(widget=forms.Select(choices=GRAU, attrs={'class': 'form-control grau_ajax'}))
    #estudante = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    #data_inscricao= forms.CharField(max_length=13,  widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = Inscricao
        fields = ['curso', 'opcao', 'periodo', 'data_inscricao', 'responsavel', 'numero_recibo']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control ajax_curso_especialidade'}),
            'periodo': forms.Select(attrs={'class': 'form-control '}),
            'opcao': forms.Select(attrs={'class': 'form-control '}),
            'data_inscricao': forms.DateInput( attrs={'class': 'form-control id-Data'}),
        }

