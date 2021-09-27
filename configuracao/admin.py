from django.contrib import admin
from configuracao.models import Curso, Provincia, Tremestre, Pais, Periodo, Grau_academico, Municipio,Genero, Resultado_Inscricao
# Register your models here.

admin.site.register(Curso)
admin.site.register(Provincia)
admin.site.register(Tremestre)
admin.site.register(Pais)
admin.site.register(Periodo)
admin.site.register(Grau_academico)
admin.site.register(Municipio)
admin.site.register(Genero)
admin.site.register(Resultado_Inscricao)