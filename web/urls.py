# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30

from django.conf.urls import url,include
from web import views
app_name = 'site'
"""
    Definicion de URLs del Sitio Web

"""
urlpatterns = [
    # '/' Vista Index de Sitio Web
    url(r'^$', views.index,name='index'),
]