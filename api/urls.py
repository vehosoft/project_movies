# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30

from django.conf.urls import url,include
from api import views

app_name = 'api'
"""
    Definicion de URLs del API REST
    
"""
urlpatterns = [
    #Para el modelo: Pelicula
    # 'api/login' Realiza la autentica usuario
    url(r'login', views.api_login,name='login'),

    # 'api/logout' Realiza el logout de un usuario
    url(r'logout', views.api_logout,name='logout'),

    # 'api/registro' Permite realizar un registro de usuario
    url(r'registro', views.api_registro, name='registro'),

    #Para el modelo: Pelicula
    # 'api/pelicula/' Muestra el listado de peliculas para el panel de administracion
    url(r'^pelicula/$', views.pelicula_list, name='pelicula'),

    # 'api/pelicula/desactivar$' Desactiva un registro pelicula
    url(r'^pelicula/desactivar$', views.pelicula_desactivar, name='pelicula_desactivar'),

    # 'api/pelicula/activar$' Activa un registro pelicula
    url(r'^pelicula/activar$', views.pelicula_activar, name='pelicula_activar'),

    # 'api/pelicula/registrar' Crea un registro de pelicula
    url(r'^pelicula/registrar', views.pelicula_registrar, name='pelicula_registrar'),

    # 'api/pelicula/actualizar' Actualiza un registro de pelicula
    url(r'^pelicula/actualizar', views.pelicula_actualizar, name='pelicula_actualizar'),

    # 'api/pelicula/subir_poster' Guarda el poster de en un registro de pelicula
    url(r'^pelicula/subir_poster', views.pelicula_subir_poster, name='pelicula_subir_poster'),

    # 'api/pelicula/lista' Obtine la lista de peliculas activas
    url(r'^pelicula/lista', views.pelicula_lista, name='pelicula_lista'),

    # 'api/pelicula/detalle' Obtine un registro de pelicula
    url(r'^pelicula/detalle', views.pelicula_detalle, name='pelicula_detalle'),

    # 'api/pelicula/comentario' Registra un comentario de pelicula
    url(r'^pelicula/comentario', views.pelicula_comentario, name='pelicula_comentario'),
]