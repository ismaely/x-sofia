# Generated by Django 3.2.4 on 2021-09-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_pessoa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='uploads/fotos/% Y/'),
        ),
    ]
