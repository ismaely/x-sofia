# Generated by Django 3.2.4 on 2021-10-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0011_alter_pessoa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, default='user.jpg', null=True, upload_to='fotos/%Y/'),
        ),
    ]
