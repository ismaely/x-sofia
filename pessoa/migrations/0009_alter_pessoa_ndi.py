# Generated by Django 3.2.4 on 2021-10-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0008_auto_20211016_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='ndi',
            field=models.CharField(max_length=40),
        ),
    ]