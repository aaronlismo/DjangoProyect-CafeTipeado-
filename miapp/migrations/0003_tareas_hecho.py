# Generated by Django 4.2.3 on 2023-07-31 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_tareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='hecho',
            field=models.BooleanField(default=False),
        ),
    ]