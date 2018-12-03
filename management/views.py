# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30
from django.template import loader, Context
from django.shortcuts import render
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import logout

"""
URL: mgm/
Metodo: index
Descripcion: 
    Renderiza la vista Index de Panel de Administracion, 
    si el usuario no esta autenticado se redirecciona a la vista Login
"""
def index(request):
    if request.user.is_authenticated and request.user.is_staff:
        context = {
            'user_name':request.user.first_name,
        }
        return render(request, 'content.html', context)
    else:
        return redirect('%s?next=%s' % ('login', request.path))

"""
URL: mgm/login
Metodo: mgm_login
Descripcion: 
    Renderiza la vista Login de Panel de Administracion, 
    si el usuario esta autenticado se redirecciona a la vista Index
"""
def mgm_login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {})
    else:
        return redirect(index)

"""
URL: mgm/logout
Metodo: mgm_logout
Descripcion: 
    Realiza el logout de una usuario, 
    redirecciona a la vista Login
"""
def mgm_logout(request):
    logout(request)
    return redirect('mgm:login')