# Generated by Django 3.1.7 on 2021-02-20 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0016_remove_plataforma_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plataforma',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]