# Generated by Django 3.1.7 on 2021-02-20 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0010_auto_20210219_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plataforma',
            old_name='usuario',
            new_name='funcionario',
        ),
    ]
