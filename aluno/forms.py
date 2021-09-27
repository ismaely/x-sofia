from django import forms
from django.db.models import Q
from django.forms import ModelForm
from pessoa.models import Pessoa
from configuracao.models import Curso, Periodo
from aluno.models import Aluno, Inscricao
import math


class Inscricao_Form(ModelForm):
    referencia = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nota_final = forms.CharField(max_length=3,error_messages={'required': 'Este campo é obrigatorio'}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Inscricao
        fields = ['curso', 'instituicao_origem', 'periodo', 'data_inscricao', 'operador']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control '}),
            'periodo': forms.Select(attrs={'class': 'form-control '}),
            'resultado': forms.Select(attrs={'class': 'form-control '}),
            'data_inscricao': forms.DateInput( attrs={'class': 'form-control'}),
        }

    def clean_nota_final(self):
        nota_final = self.cleaned_data.get('nota_final')
        if int(nota_final) > 9 and int(nota_final) <= 20:
            return nota_final
        elif int(nota_final) > 20:
            nota_final = (int(nota_final) * 20)/100
            return math.trunc(nota_final)
        else:
            raise forms.ValidationError("A media final não é valida")
