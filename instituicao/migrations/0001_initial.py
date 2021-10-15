# Generated by Django 3.2.4 on 2021-10-14 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=260, null=True)),
                ('localizacao', models.CharField(blank=True, default=' ', max_length=250, null=True)),
                ('telefone', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('email', models.CharField(blank=True, default=' ', max_length=250, null=True)),
                ('municipio', models.CharField(blank=True, default=' ', max_length=150, null=True)),
                ('data_fundacao', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('data_create', models.DateField(auto_now=True)),
            ],
        ),
    ]