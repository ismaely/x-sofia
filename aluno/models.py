"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-09-26 12:36:58
 * @modify date 2021-09-26 12:36:58
 * @desc [description]
 */
 """

from django.db import models
#from pessoa.models import Pessoa
from configuracao.models import Curso, Resultado_Inscricao, Periodo, Grau_academico

# Create your models here.
"""
class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    #numero_estudante= models.CharField(max_length=30, blank=True, null=True, default="NULL")
    media_conclusao = models.CharField(max_length=3, blank=True, null=True)
    instituicao_origem = models.CharField(max_length=120, blank=True, null=True,default="")
    data_registro = models.CharField(max_length=20)
    data_create= models.DateField(auto_now=True)

    def __str__ (self):
        return self.id
    class Meta:
        order_with_respect_to = 'pessoa'
"""

        
"""class Inscricao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, blank=True, null=True, parent_link=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, parent_link=True)
    media_conclusao = models.CharField(max_length=3, blank=True, null=True, default="")
    instituicao_origem = models.CharField(max_length=120, blank=True, null=True,default="")
    data_inscricao = models.CharField(max_length=20)
    operador = models.CharField(max_length=190, blank=True, null=True)
    ano_conclusao = models.CharField(max_length=3, blank=True, null=True, default="")
    habilitacao_literaria = models.ForeignKey(Grau_academico, on_delete=models.CASCADE, parent_link=True)
    numero_inscricao = models.CharField(max_length=10, blank=True, null=True,default="")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id
"""

"""class InscricaoResultado(models.Model):
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE, parent_link=True)
    resultado = models.ForeignKey(Resultado_Inscricao, on_delete=models.DO_NOTHING, blank=True, null=True, parent_link=True)
    descricao = models.CharField(max_length=3, blank=True, null=True, default="")
    data = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    operador = models.CharField(max_length=190, blank=True, null=True)

    def __str__ (self):
        return self.id
"""