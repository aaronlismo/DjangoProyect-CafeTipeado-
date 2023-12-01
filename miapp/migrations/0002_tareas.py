# Generated by Django 4.2.3 on 2023-07-26 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.proyecto')),
            ],
        ),
    ]