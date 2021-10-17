# Generated by Django 3.2.4 on 2021-10-17 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0007_delete_inscricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.pessoa')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, to='configuracao.curso')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='configuracao.periodo')),
                ('media_conclusao', models.CharField(blank=True, default='', max_length=3, null=True)),
                ('instituicao_origem', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('data_inscricao', models.CharField(max_length=20)),
                ('operador', models.CharField(blank=True, max_length=190, null=True)),
                ('ano_conclusao', models.CharField(blank=True, default='', max_length=3, null=True)),
                ('habilitacao_literaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='configuracao.grau_academico')),
                ('numero_inscricao', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
