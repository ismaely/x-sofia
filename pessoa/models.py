from django.db import models
from configuracao.models import Pais, Provincia, Municipio, Genero, Estado_Civil, Documento_identificacao

# Create your models here.
""""""
class Pessoa(models.Model):
    nome = models.CharField(max_length=200,)
    nome_pai = models.CharField(max_length=200, blank=True, null=True, default="")
    nome_mae = models.CharField(max_length=200, blank=True, null=True, default="")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    data_nascimento=models.CharField(max_length=20)
    ndi = models.CharField(max_length=40,  blank=True, null=True, default="")
    estado_civil = models.ForeignKey(Estado_Civil, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    residencia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True, default="")
    email = models.EmailField(max_length=190, blank=True, null=True, default="")
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, parent_link=True, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, parent_link=True,  blank=True, null=True, default="")
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE, parent_link=True, default=6)
    data_create= models.DateField(auto_now=True)
    foto = models.FileField(upload_to='uploads/fotos/% Y/', blank=True, null=True)
    documento = models.ForeignKey(Documento_identificacao, on_delete=models.CASCADE, parent_link=True)
    def __str__(self):
        return self.id
