# Generated by Django 3.2.4 on 2021-09-08 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=60, null=True)),
                ('data_create', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Civil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='configuracao.provincia')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=60, null=True)),
            ],
        ),
    ]
