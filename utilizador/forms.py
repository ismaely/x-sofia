from django import forms
from django.db.models import Q
from django.forms import ModelForm



class LoginForm(forms.Form):
    senha = forms.CharField(max_length=90, widget=forms.PasswordInput(attrs={'class': 'form-text'}))
    nome = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-text'}))

