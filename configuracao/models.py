"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-09-26 12:54:22
 * @modify date 2021-09-26 12:54:22
 * @desc [description]
 */
"""

from django.db import models
import uuid

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=190)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__ (self):
        return "%s" % (self.nome)


class Tremestre(models.Model):
    nome = models.CharField(max_length=100,  blank=True, null=True)
    def __str__(self):
        return  "%s" % (self.nome)



class Provincia(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    def __str__ (self):
        return  "%s" % (self.nome)



class Grau_academico(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)


class Periodo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nome)


class Pais(models.Model):
    nome = models.CharField(max_length=100,  default="")
    nacionalidade = models.CharField(max_length=50, blank=True, null=True, default=" ")
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)


class Municipio(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, parent_link=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)



class Estado_Civil(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nome)



class Genero(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)

class Resultado_Inscricao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)

class Documento_identificacao(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3, blank=True, null=True, default=" ")
    descricao = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__(self):
        return "%s" % (self.nome)