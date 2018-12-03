# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30
from django.shortcuts import render
"""
URL: /
Metodo: index
Descripcion: 
    Renderiza la vista Index de Sitio Web
"""
def index(request):
    return render(request, 'listado.html', {})
