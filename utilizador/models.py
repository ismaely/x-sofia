from django.db import models
from django.contrib.auth.models import User
from configuracao.models import Genero

# Create your models here.

class Utilizador(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING, parent_link=True)
    ndi = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=30, blank=True, null=True, default="")
    morada = models.CharField(max_length=90, blank=True, null=True)
    estado = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)
    categoria = models.CharField(max_length=90, blank=True, null=True, default="")

    def __str__(self):
        return self.id