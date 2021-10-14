
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

app_name = 'instituicao'
urlpatterns = [
    path('nova-instituicao/', views.nova_instituica, name="nova-instituicao"),
]
