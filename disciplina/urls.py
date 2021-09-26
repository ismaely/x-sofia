"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-09-26 10:24:07
 * @modify date 2021-09-26 10:24:07
 * @desc [description]
 *
 """

  
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'disciplina'
urlpatterns = [
    path('adicionarNovaDisciplia/', views.adicionarNovaDisciplina, name= "nova-disciplina"),
    path('listarDisciplina/', views.listarDisciplina, name= "listar-disciplina"),
]
