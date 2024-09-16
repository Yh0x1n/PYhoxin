# Generated by Django 5.1.1 on 2024-09-16 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del autor')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_fallecimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de fallecimiento')),
                ('profesion', models.CharField(max_length=50, verbose_name='Profesión')),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='FraseDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cita', models.TextField(max_length=500, verbose_name='Cita')),
                ('autor_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.authordb')),
            ],
        ),
    ]