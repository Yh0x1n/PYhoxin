from typing import Any
from django.db import models

# Create your models here.

class AuthorDB(models.Model):
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre del autor')
    fecha_nacimiento = models.DateField(verbose_name = 'Fecha de nacimiento', null = False)
    fecha_fallecimiento = models.DateField(verbose_name = 'Fecha de fallecimiento', null = True, blank = True)
    profesion = models.CharField(verbose_name = 'Profesión', max_length = 50)
    nacionalidad = models.CharField(verbose_name = 'Nacionalidad', max_length = 50)

    class Meta:
        db_table = 'Autores'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self) -> str:
        return self.nombre

class FraseDB(models.Model):
    cita = models.TextField(max_length=500, verbose_name = 'Cita')
    autor_fk = models.ForeignKey(AuthorDB, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Frase'
        verbose_name_plural = 'Frases'

    def __str__(self) -> str:
        return self.cita