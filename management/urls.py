# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30

from django.conf.urls import url,include
from management.views import index,mgm_logout
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'mgm'
"""
    Definicion de URLs del Panel Administrador de Peliculas

"""
urlpatterns = [
    # 'mgm/' Vista Index de Panel de Administracion
    url(r'^$', index,name='index'),

    # 'mgm/login' Vista Login de Panel de Administracion
    url(r'login/$', LoginView.as_view(template_name='login.html'),name='login'),

    # 'mgm/logout' Logout de usuarios, retorna a la vista Index de Panel de Administracion
    url(r'logout/$', mgm_logout, name='logout'),
]