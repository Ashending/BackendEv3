# Generated by Django 5.1.3 on 2024-11-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='activo',
            field=models.IntegerField(choices=[(1, 'Activo'), (0, 'Inactivo')]),
        ),
    ]
