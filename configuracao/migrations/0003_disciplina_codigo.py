# Generated by Django 3.2.4 on 2021-09-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao', '0002_disciplina_estado_civil_genero_municipio'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='codigo',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
