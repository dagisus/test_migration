from __future__ import unicode_literals

from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=255)


class Tema(models.Model):
    nombre = models.CharField(max_length=255)


class Libro(models.Model):
    autor = models.ManyToManyField(Autor)
    tema = models.ForeignKey(Tema)
    nombre = models.CharField(max_length=255)
    publicacion = models.DateField()