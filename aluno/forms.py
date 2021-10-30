from django import forms
from django.db.models import Q
from django.forms import ModelForm
from pessoa.models import Pessoa
from configuracao.models import Curso, Periodo
from aluno.models import Aluno, Inscricao
import math


class Inscricao_Form(ModelForm):
    ndi = forms.CharField(max_length=14,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instituicao_origem = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_conclusao = forms.CharField(max_length=4,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    media_conclusao = forms.CharField(max_length=3,required=False, error_messages={'required': 'Este campo é obrigatorio'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Inscricao
        fields = ['curso', 'instituicao_origem', 'periodo', 'data_inscricao', 'operador', 'ano_conclusao','habilitacao_literaria']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control ajax_curso', 'disabled':'disabled'}),
            'periodo': forms.Select(attrs={'class': 'form-control '}),
            'habilitacao_literaria': forms.Select(attrs={'class': 'form-control ajax_classeFrequencia'}),
            'data_inscricao': forms.DateInput( attrs={'class': 'form-control','type': 'date'}),
        }

    """def clean_nota_final(self):
        nota_final = self.cleaned_data.get('nota_final')
        if int(nota_final) > 9 and int(nota_final) <= 20:
            return nota_final
        elif int(nota_final) > 20:
            nota_final = (int(nota_final) * 20)/100
            return math.trunc(nota_final)
        else:
            raise forms.ValidationError("A media final não é valida")
    """


class Listar_inscricao_Form(forms.Form):
    classe = forms.CharField(widget=forms.Select(choices = '' , attrs={'class': 'form-control'}))
    genero = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control'}))
    periodo = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_ano'}))
    curso = forms.CharField(required=False, widget=forms.Select(choices='', attrs={'class': 'form-control ajax_curso'}))
    dataInscricao = forms.CharField(required=False, max_length=13, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    dataFim = forms.CharField(max_length=13, required=False, widget=forms.TextInput(attrs={'type': 'date','class': 'form-control'}))

