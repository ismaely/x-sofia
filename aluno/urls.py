
from django.contrib import admin
from django.urls import path
from django.conf import settings

app_name = 'aluno'
urlpatterns = [
    path('admin/', admin.site.urls),
]
