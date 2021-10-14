from django.db import models

# Create your models here.

class Instituicao(models.Model):
    nome = models.CharField(max_length=100,  default="")
    sigla = models.CharField(max_length=260, blank=True, null=True, default=" ")
    localizacao = models.CharField(max_length=250, blank=True, null=True, default=" ")
    telefone = models.CharField(max_length=50, blank=True, null=True, default=" ")
    email = models.CharField(max_length=250, blank=True, null=True, default=" ")
    municipio = models.CharField(max_length=150, blank=True, null=True, default=" ")
    data_fundacao = models.CharField(max_length=50, blank=True, null=True, default=" ")
    data_create= models.DateField(auto_now=True)



    def __str__(self):
        return "%s" % (self.nome)