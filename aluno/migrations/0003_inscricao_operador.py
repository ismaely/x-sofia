# Generated by Django 3.2.4 on 2021-09-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_inscricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='operador',
            field=models.CharField(blank=True, max_length=190, null=True),
        ),
    ]