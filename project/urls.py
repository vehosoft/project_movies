# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

"""
    Definicion de URLs del Proyecto

"""
urlpatterns = [
    # '/' Incluye a todas las urls definidas en web para el Sitio Web
    path('', include('web.urls')),

    # 'api/' Incluye a todas las urls definidas en api para el API REST
    url(r'api/', include('api.urls')),

    # 'mgm/' Incluye a todas las urls definidas en management para el Panel de Administracion
    url(r'mgm/', include('management.urls')),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
