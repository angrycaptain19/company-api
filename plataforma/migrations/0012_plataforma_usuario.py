# Generated by Django 3.1.7 on 2021-02-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('plataforma', '0011_auto_20210219_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataforma',
            name='usuario',
            field=models.ManyToManyField(to='usuarios.Usuario'),
        ),
    ]
