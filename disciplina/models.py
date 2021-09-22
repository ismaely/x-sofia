from django.db import models

# Create your models here.


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    codigo = models.CharField(max_length=20, blank=True, null=True, default="")
    data_create= models.DateField(auto_now=True)

    def __str__(self):
        return "%s" % (self.nome)

