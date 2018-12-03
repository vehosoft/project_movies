# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30
import datetime
from django.db import models
from django.conf import settings

"""
    Modelo: Pelicula
    Atributos:
        - titulo, Titulo de la Pelicula
        - sinopsis, Descripcion corta de la Pelicula
        - poster, Imagen en formato binario del poster de la Pelicula
        - resena, Descripcion amplia de la Pelicula
        - fecha_estreno, Fecha de estreno de la Pelicula, en formato YYYY-mm-dd
        - active, Estado activo de la Pelicula, si es True se muestra en el sitio web

"""
class Pelicula(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    sinopsis = models.TextField('Sinopsis')
    poster = models.BinaryField('Poster', blank=True, null=True)
    resena = models.TextField('Reseña', )
    fecha_estreno = models.DateField('Fecha de estreno', default=datetime.date.today)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

"""
    Modelo: Comentario
    Atributos:
        - comentario
        - fecha, Fecha de registro del comentario, en formato YYYY-mm-dd
        - pelicula_id, id de la Pelicula a que se relaciona el comentario
        - usuario_id, id del Usuario que registro el comentario

"""
class Comentario(models.Model):
    comentario = models.TextField('Comentario')
    fecha = models.DateField("Fecha",default=datetime.date.today)
    pelicula_id = models.ForeignKey(Pelicula, related_name='comentarios', on_delete=models.DO_NOTHING)
    usuario_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', blank=True, null=True,
                                  related_name="comentarios", on_delete=models.DO_NOTHING)