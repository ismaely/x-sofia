from django.db import models
from pessoa.models import Pessoa
from disciplina.models import Disciplina

# Create your models here.
class Docente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    graduacao = models.CharField(max_length=100, blank=True, null=True, default="")
    categoria = models.CharField(max_length=200, blank=True, null=True, default="")
    funcao = models.CharField(max_length=190, blank=True, null=True, default="")
    data_create= models.DateField(auto_now=True)

    def __str__(self):
        return "%d" % (self.id)



class Docente_Disciplina(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, parent_link=True)
    estado = models.CharField(max_length=19, blank=True, null=True, default="Ativado")
    data_registro = models.CharField(max_length=20)
    data_create= models.DateField(auto_now=True)

    def __str__ (self):
        return self.id