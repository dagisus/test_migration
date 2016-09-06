from __future__ import unicode_literals

from django.db import models


class Autor(models.Model):
    nombre = models.CharField()


class Tema(models.Model):
    nombre = models.CharField()


class Libro(models.Model):
    autor = models.ManyToManyField(Autor)
    tema = models.ForeignKey(Tema)
    nombre = models.CharField()
    publicacion = models.DateField()