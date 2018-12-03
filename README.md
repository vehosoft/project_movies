# project_movies
Proyecto de Sitio Web de Reseñas Peliculas con Panel de Administracion y API REST

Panel de Administracion: Administra los registros de Peliculas por usuarios STTAF

![PanelAdmin](/static/img/PanelAdmin.png "PanelAdmin")


Sitio Web: Muestra peliculas, reseñas y comentarios, permite el registro de comentarios de 
usuarios autenticados 

![SitioWeb](/static/img/SitioWeb.png "SitioWeb")

### Lenguajes
* Python 3
* SQLite
* JavaScript

### FrameWorks
* Django
* VueJS

### Librerias
* Bootstrap

### Project Structure


| Location                                    |  Content                                      |
|---------------------------------------------|-----------------------------------------------|
| `/api`                                      | API REST                                      |
| `/api/models.py`                            | Declaracion de modelos Pelicula y Comentario  |
| `/api/urls.py`                              | Declaracion de URLs del API REST              |
| `/api/views.py`                             | Declaracion de metodos del API REST           |
| `/management`                               | App Panel de Administracion de Peliculas      |
| `/project`                                  | Project Config                                |
| `/static`                                   | STATIC FILES                                  |
| `/static/js/site.js`                        | VUE App Web Site                              |
| `/static/management`                        | Estructura VUE App Panel de Admin             |
| `/static/management/main.js`                | VUE App Panel de Admin                        |
| `/static/management/component/Pelicula.vue` | VUE Component Pelicula para Panel de Admin    |
| `/web`                                      | App Web Site de reseña de Peliculas           |
| `/db.sqlite3`                               | Base de Datos                                 |

## Prerequisites

- [X] NPM - [instructions](https://www.npmjs.com/get-npm)
- [X] Python 3
- [X] Pip

## Setup Project

```
$ git clone https://github.com/vehosoft/project_movies.git
$ cd project_movies
```

Setup
```
$ python3.x -m venv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ cd static
$ npm install
$ cd ..

```

## Running Development Servers

```
$ python manage.py runserver
```
## Accesos

[Web Site](http://localhost:8000/)

[Panel de Administracion](http://localhost:8000/mgm)

Super Usuario
* username: frodriguez@vehosoft.com
* password: 123
