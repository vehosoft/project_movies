# -*- coding: utf-8 -*-
# @Author: Francisco Rodriguez
# @Date:   2018-11-30
# @Last Modified by:   Francisco Rodriguez
# @Last Modified: 2018-11-30

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from api.models import Pelicula,Comentario

"""
URL: api/registro
URL Method: POST
Metodo: api_registro
Descripcion: Permite realizar un registro de usuario
Parametros: 
    - nombre
    - email
    - password
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def api_registro(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            print(request.POST)
            try:
                user = User(username=request.POST['email'])
                user.first_name = request.POST['nombre']
                user.set_password(request.POST['password'])
                user.email = request.POST['email']
                user.save()
                return JsonResponse({'success': True})

            except IOError as e:
                pass
    return JsonResponse({'success': False})

"""
URL: api/login
URL Method: POST
Metodo: api_login
Descripcion: Realiza la autentica usuario
Parametros: 
    - email
    - password
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def api_login(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            print(request.POST)
            try:
                user_auth = authenticate(
                    request, username=request.POST['email'],
                    password=request.POST['password']
                )
                if user_auth is not None:
                    login(request, user_auth)
                    return JsonResponse({'success': True})
            except IOError as e:
                pass
    return JsonResponse({'success': False})

"""
URL: api/logout
URL Method: POST,GET
Metodo: api_logout
Descripcion: Realiza el logout de un usuario
Parametros: ninguno
Respuesta: redirecciona a la vista index
"""
@csrf_exempt
def api_logout(request):
    logout(request)
    return redirect('site:index')

"""
URL: api/pelicula/lista
URL Method: GET
Metodo: pelicula_lista
Descripcion: Obtiene una lista simplificada de registros activos (active=True) del modelo Pelicula ordenada por fecha_estreno(desc) y titulo
Parametros: 
    - page (opcional), si se utiliza paginado page es la pagina solicitada
    - per_page (opcional), es el numero de registros por pagina, por defecto es 10
Respuesta: Objeto JSON 
    {
        success =  [True,False]
        records = list(Peliculas), con los parametros: titulo, sinopsis, poster y fecha_estreno
        pagination = Objeto Paginacion
    }
"""
@csrf_exempt
def pelicula_lista(request):
    if request.method == "GET":
        peliculas = Pelicula.objects.filter(active=True).order_by('-fecha_estreno','titulo').values('id','titulo','sinopsis','fecha_estreno','poster')
        index = 0
        for rec in peliculas:
            peliculas[index]['poster'] = rec['poster'].decode(encoding="utf-8");
            index += 1

        per_page = 10
        if request.GET.get('per_page'):
            per_page = request.GET['per_page']

        if request.GET.get('page'):
            p = Paginator(peliculas, per_page)
            page = p.page(request.GET['page'])
            pagination = {
                'total': peliculas.count(),
                'current_page': request.GET['page'],
                'per_page': per_page,
                'last_page': p.num_pages,
                'from': page.start_index(),
                'to': page.end_index(),
            }
        else:
            p = Paginator(peliculas, peliculas.count())
            page = p.page(1)
            pagination = {
                'total': peliculas.count(),
                'current_page': 1,
                'per_page': per_page,
                'last_page': p.num_pages,
                'from': page.start_index(),
                'to': page.end_index(),
            }

        resp = {
            'success': True,
            'records':list(page.object_list),
            'pagination': pagination,
        }

        return  JsonResponse(resp, safe=False)
    return JsonResponse({'success': False})

"""
URL: api/pelicula/detalle
URL Method: GET
Metodo: pelicula_detalle
Descripcion: Obtiene un registro del modelo Pelicula correspondiente un id
Parametros: 
    - pk
Respuesta: Objeto JSON 
    {
        success =  [True,False]
        record= Pelicula
    }
"""
@csrf_exempt
def pelicula_detalle(request):
    print(request.method)
    print(request.GET)
    if request.method == 'GET':
        try:
            peliculas = Pelicula.objects.filter(pk=request.GET['pk']).values(
                'id', 'titulo', 'sinopsis', 'poster','resena','fecha_estreno','comentarios'
            )
            index = 0
            for rec in peliculas:
                peliculas[index]['poster'] = rec['poster'].decode(encoding="utf-8");
                print(rec['comentarios'])
                if type(rec['comentarios']) is int and rec['comentarios'] > 0:
                    comentarios = Comentario.objects.filter(pelicula_id=rec['id'])
                    lista_comentarios = []
                    for comentario in comentarios:
                        lista_comentarios.append({
                            'usuario': comentario.usuario_id.first_name,
                            'comentario': comentario.comentario,
                            'fecha': comentario.fecha
                        })
                    print(lista_comentarios)
                    peliculas[index]['comentarios'] = list(lista_comentarios)
                else:
                    peliculas[index]['comentarios'] = []
                index += 1
            return JsonResponse({'success':True,'record':list(peliculas)[0]}, safe=False)
        except IOError as e:
            pass
    return JsonResponse({'success': False})

"""
URL: api/pelicula/comentario
URL Method: POST
Metodo: pelicula_comentario
Descripcion: Permite registrar un comentario
Parametros: 
    - pelicula_id
    - comentario
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_comentario(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                pelicula = Pelicula.objects.get(pk=request.POST['pelicula_id'])
                usuario = User.objects.get(username=request.user.username)
                Comentario.objects.create(
                    comentario= request.POST['comentario'],
                    pelicula_id= pelicula,
                    usuario_id= usuario
                )
                return JsonResponse({'success': True})

            except IOError as e:
                pass


    return JsonResponse({'success': False})

"""
URL: api/pelicula/registrar
URL Method: POST
Metodo: pelicula_registrar
Descripcion: Permite crear un registro de pelicula
Parametros: 
    - titulo
    - sinopsis
    - resena
    - fecha_estreno
    - poster, en formato base64 codificado
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_registrar(request):
    if request.method == "POST":
        try:
            pelicula = Pelicula()
            pelicula.titulo = request.POST['titulo']
            pelicula.sinopsis = request.POST['sinopsis']
            pelicula.resena = request.POST['resena']
            pelicula.fecha_estreno = request.POST['fecha_estreno']
            pelicula.poster = bytes(request.POST['poster'], 'utf-8')
            pelicula.save()
            return JsonResponse({'success':True})
        except IOError as e:
            pass
    return JsonResponse({'success': False})

"""
URL: api/pelicula/
URL Method: GET
Metodo: pelicula_list
Descripcion: Obtiene una lista de registros del modelo Pelicula ordenada por fecha_estreno(desc) y titulo
Parametros: 
    - page (opcional), si se utiliza paginado page es la pagina solicitada
    - per_page (opcional), es el numero de registros por pagina, por defecto es 10
Respuesta: Objeto JSON 
    {
        success =  [True,False]
        records = list(Peliculas), con los parametros: todos
        pagination = Objeto Paginacion
    }
"""
@csrf_exempt
def pelicula_list(request):
    if request.method == "GET":
        peliculas = Pelicula.objects.all().order_by('-fecha_estreno','titulo').values()
        index = 0
        for rec in peliculas:
            peliculas[index]['poster'] = rec['poster'].decode(encoding="utf-8");
            index += 1

        per_page = 10
        if request.GET.get('per_page'):
            per_page = request.GET['per_page']

        if request.GET.get('page'):
            p = Paginator(peliculas, per_page)
            page = p.page(request.GET['page'])
            pagination = {
                'total': peliculas.count(),
                'current_page': request.GET['page'],
                'per_page': per_page,
                'last_page': p.num_pages,
                'from': page.start_index(),
                'to': page.end_index(),
            }
        else:
            p = Paginator(peliculas, peliculas.count())
            page = p.page(1)
            pagination = {
                'total': peliculas.count(),
                'current_page': 1,
                'per_page': per_page,
                'last_page': p.num_pages,
                'from': page.start_index(),
                'to': page.end_index(),
            }

        resp = {
            'records':list(page.object_list),
            'pagination': pagination,
        }

        return  JsonResponse(resp, safe=False)
    return JsonResponse({'success': False})

"""
URL: api/pelicula/desactivar
URL Method: POST
Metodo: pelicula_desactivar
Descripcion: Desactiva un registro de Pelicula, por medio del parametro active=False, cuando es False no se muestra en Sitio Web
Parametros: 
    - pk
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_desactivar(request):
    if request.method == 'POST':
        try:
            pelicula = Pelicula.objects.get(pk=request.POST['pk'])
            pelicula.active = False
            pelicula.save()
            return JsonResponse({'success':True})
        except IOError as e:
            pass
    return JsonResponse({'success': False})

"""
URL: api/pelicula/activar
URL Method: POST
Metodo: pelicula_activar
Descripcion: Activa un registro de Pelicula, por medio del parametro active=True
Parametros: 
    - pk
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_activar(request):
    if request.method == "POST":
        try:
            pelicula = Pelicula.objects.get(pk=request.POST['pk'])
            pelicula.active = True
            pelicula.save()
            return JsonResponse({'success':True})
        except IOError as e:
            pass
    return JsonResponse({'success': False})

"""
URL: api/pelicula/actualizar
URL Method: POST
Metodo: pelicula_actualizar
Descripcion: Actualiza un registro de Pelicula
Parametros: 
    - pk
    - titulo
    - sinopsis
    - resena
    - fecha_estreno
    
Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_actualizar(request):
    if request.method == "POST":
        try:
            pelicula = Pelicula.objects.get(pk=request.POST['pk'])
            pelicula.titulo = request.POST['titulo']
            pelicula.sinopsis = request.POST['sinopsis']
            pelicula.resena = request.POST['resena']
            pelicula.fecha_estreno = request.POST['fecha_estreno']
            pelicula.save()
            return JsonResponse({'success':True})
        except IOError as e:
            pass
    return JsonResponse({'success': False})


"""
URL: api/pelicula/subir_poster
URL Method: POST
Metodo: pelicula_subir_poster
Descripcion: Actualiza el poster de un registro de Pelicula
Parametros: 
    - pk
    - poster, en formato base64 codificado

Respuesta: Objeto JSON 
    {
        success =  [True,False]
    }
"""
@csrf_exempt
def pelicula_subir_poster(request):
    if request.method == 'POST':
        if request.POST.get('poster'):
            try:
                pelicula = Pelicula.objects.get(pk=request.POST['pk'])
                pelicula.poster = bytes(request.POST['poster'], 'utf-8')
                pelicula.save()
                return JsonResponse({'success': True})
            except IOError as e:
                pass
    return JsonResponse({'success': False})
