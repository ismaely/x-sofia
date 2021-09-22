# Generated by Django 3.2.4 on 2021-09-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, to='configuracao.genero')),
                ('bi', models.CharField(max_length=20, unique=True)),
                ('telefone', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('morada', models.CharField(blank=True, max_length=90, null=True)),
                ('estado', models.CharField(max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.user')),
            ],
        ),
    ]
