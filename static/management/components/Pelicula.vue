{% load static %}
<template>
    <main class="main">
        <!-- Breadcrumb -->
        <ol class="breadcrumb">
            <li class="breadcrumb-item active">Peliculas</li>
        </ol>
        <div class="container-fluid">
            <!-- Ejemplo de tabla Listado -->
            <div class="card">
                <div class="card-header">
                    <i class="fa fa-align-justify"></i> Peliculas
                    <button type="button" @click="abrirModal('registrar')" class="btn btn-primary pull-right">
                        <i class="icon-plus"></i>&nbsp;Nuevo
                    </button>
                </div>
                <div class="card-body">

                    <table class="table table-bordered table-striped table-sm">
                        <thead>
                            <tr>
                                <th>Poster</th>
                                <th>Titulo</th>
                                <th>Fecha de estreno</th>
                                <th>Estado</th>
                                <th>Opciones</th>
                            </tr>
                        </thead>
                        <tbody>

                            <tr v-for="rec in array" :key="rec.id">
                                <td> <img class="preview-table" :src="rec.poster"> </td>
                                <td v-text="rec.titulo"></td>
                                <td v-text="rec.fecha_estreno"></td>
                                <td>
                                    <div v-if="rec.active">
                                        <span class="badge badge-success">Activo</span>
                                    </div>
                                    <div v-else>
                                        <span class="badge badge-danger">Desactivado</span>
                                    </div>

                                </td>
                                <td>
                                    <button type="button" @click="abrirModal('actualizar',rec)" class="btn btn-warning btn-sm">
                                      <i class="icon-pencil"></i>
                                    </button>
                                    <template v-if="rec.active">
                                        <button type="button" @click="desactivar(rec.id)" class="btn btn-danger btn-sm">
                                            <i class="icon-lock"></i>
                                        </button>
                                    </template>
                                    <template v-else>
                                        <button type="button" @click="activar(rec.id)" class="btn btn-info btn-sm">
                                            <i class="icon-lock-open"></i>
                                        </button>
                                    </template>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <nav>
                        <ul class="pagination">
                            <li class="page-item" v-if="pagination.current_page > 1">
                                <a class="page-link" href="#" @click.prevent="cambiarPagina(pagination.current_page - 1)">Ant</a>
                            </li>
                            <li class="page-item" v-for="page in pagesNumber" :key="page" :class="[page == pagesActived ? 'active':'']">
                                <a class="page-link" href="#" v-text="page" @click.prevent="cambiarPagina(page)"></a>
                            </li>
                            <li class="page-item" v-if="pagination.current_page < pagination.last_page">
                                <a class="page-link" href="#" @click.prevent="cambiarPagina(pagination.current_page + 1)">Sig</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
            <!-- Fin ejemplo de tabla Listado -->
        </div>
        <!--Inicio del modal agregar/actualizar-->
        <div class="modal fade" tabindex="-1" :class="{'mostrar':modal}" role="dialog" aria-labelledby="myModalLabel" style="display: none;" aria-hidden="true">

            <div class="modal-dialog modal-primary modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 v-text="titulo_modal" class="modal-title"></h4>
                        <button type="button" class="close" @click="modal=0" aria-label="Close">
                          <span aria-hidden="true">×</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form action="" method="post" enctype="multipart/form-data" class="form-horizontal">
                            <div class="form-group row">
                                <label class="col-md-3 form-control-label" for="text-input">Titulo (*)</label>
                                <div class="col-md-9">
                                    <input type="text" v-model="titulo" class="form-control" placeholder="Titulo de pelicula">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label class="col-md-3 form-control-label" for="text-input">Sinopsis (*)</label>
                                <div class="col-md-9">
                                    <textarea v-model="sinopsis" class="form-control" placeholder="Sinopsis de pelicula" rows="3"></textarea>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label class="col-md-3 form-control-label" for="text-input">Reseña (*)</label>
                                <div class="col-md-9">
                                    <textarea v-model="resena" class="form-control" placeholder="Reseña de pelicula" rows="6"></textarea>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label class="col-md-3 form-control-label" for="text-input">Fecha de estreno</label>
                                <div class="col-md-9">
                                    <input type="text" v-model="fecha_estreno" class="form-control" placeholder="AAAA-mm-dd">
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="file-upload-form col-md-6">
                                    Poster:
                                    <input type="file"  @change="previewImage" accept="image/*">
                                </div>
                                <div class="image-preview col-md-6" v-if="imageData.length > 0">
                                    <img class="preview" :src="imageData">
                                </div>

                            </div>
                            <div v-show="error" class="form-group row div-error">
                                <div class="text-center text-error">
                                    <div v-for="errorMsj in errors" :key="errorMsj" v-text="errorMsj"></div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="modal=0">Cerrar</button>
                        <button type="button" v-if="action==1" @click="registrar()" class="btn btn-primary">Guardar</button>
                        <button type="button" v-if="action==2" @click="actualizar()" class="btn btn-primary">Actualizar</button>
                    </div>
                </div>
                <!-- /.modal-content -->
            </div>
            <!-- /.modal-dialog -->
        </div>
        <!--Fin del modal-->
    </main>
</template>

<script>

/**

 * @author   Francisco Rodriguez <frodriguez@vehosoft.com>

 * History

 * v1.0 – Component VUE JS Pelicula para Panel de Administracion

 * ----

*/
    export default {
        data(){
            return{
                id: 0,
                titulo: "",
                sinopsis: "",
                resena: "",
                poster: "",
                fecha_estreno: "",
                active: 1,
                imageData: '',
                array: [],
                modal: 0,
                titulo_modal : "",
                action: 0,
                error: 0,
                errors: [],
                pagination:{
                    'total': 0,
                    'current_page': 1,
                    'per_page':  0,
                    'last_page':  1,
                    'from':  0,
                    'to':  0,
                },
                offset: 3,
                criterio: 'titulo',
                buscar: '',
                csrftoken: '',
                qs: function(){}
            }
        },
        computed: {
            pagesActived: function(){
                return this.pagination.current_page;
            },
            /**
                 * Method: pagesNumber
                 * Description: Obtiene un arreglo de numero de paginas para el paginador
                 * @return  {Array}
             */
            pagesNumber: function(){
                if(!this.pagination.to){
                    return [];
                }
                var from = this.pagination.current_page - this.offset;
                if(from < 1){
                    from = 1;
                }
                var to = from + (this.offset * 2);
                if(to >= this.pagination.last_page){
                    to = this.pagination.last_page;
                }
                var pagesArray = [];
                while(from <= to){
                    pagesArray.push(from);
                    from++;
                }

                return pagesArray;
            }
        },
        methods: {
                /**
                 * Method: previewImage
                 * Description: onChange function del campo poster, guarda la imagen en  imageData
             */
            previewImage: function(event) {
                let me = this;
                var input = event.target;
                if (input.files && input.files[0]) {
                    var reader = new FileReader();
                    reader.onload = (e) => {
                        me.imageData = e.target.result;
                    }
                    reader.readAsDataURL(input.files[0]);

                }
            },
            /**
                 * Method: listar
                 * Description: Realiza una peticion al API REST a la url api/pelicula para obtener una lista de peliculas
                 * @param: page  {int}
             */
            listar(page=false){
                let me=this;
                if(page) me.pagination.current_page = page;
                var url = '/api/pelicula?page='+me.pagination.current_page+'&buscar='+me.buscar+'&criterio='+me.criterio;
                console.log(url);
                axios.get(url)
                .then(function (response) {
                    // handle success
                    console.log(response);
                    var resp = response.data;
                    me.array = resp.records;
                    me.pagination = resp.pagination;
                })
                .catch(function (error) {
                    // handle error
                    console.log(error);
                });
            },

            /**
                 * Method: cambiarPagina
                 * Description: Camabia la pagina del paginador y llama a listar(pagina)
             */
            cambiarPagina(page){
                let me = this;
                me.listar(page);
            },

            /**
                 * Method: registrar
                 * Description: Realiza una peticion al API REST a la url api/pelicula/registrar para registrar una pelicula
                 * @param: titulo  {string}
                 * @param: sinopsis  {string}
                 * @param: resena  {string}
                 * @param: poster  {string} base64
                 * @param: fecha_estreno  {string} date YYYY-mm-dd
             */
            registrar(){
                let me = this;
                if(this.validar()){
                    return;
                }
                axios.post('/api/pelicula/registrar', me.qs.stringify({
                    titulo: me.titulo,
                    sinopsis: me.sinopsis,
                    resena: me.resena,
                    poster: me.imageData,
                    fecha_estreno: me.fecha_estreno,
                }),{
                            headers: {
                                "X-CSRFToken": me.csrfToken
                            },
                            xsrfHeaderName: "X-CSRFToken",
                })
                .then(function (response) {
                    me.modal = 0;
                    me.listar(1);
                    swal(
                        'Registrado!',
                        'La pelicula ha sido registrado.',
                        'success'
                    )
                })
                .catch(function (error) {
                    console.log(error);
                });
            },

            /**
                 * Method: actualizar
                 * Description: Realiza una peticion al API REST a la url api/pelicula/actualizar para actualizar una pelicula
                 * @param: titulo  {string}
                 * @param: sinopsis  {string}
                 * @param: resena  {string}
                 * @param: poster  {string} base64
                 * @param: fecha_estreno  {string} date YYYY-mm-dd
             */
            actualizar(){
                let me = this;
                if(me.validar()){
                    return;
                }
                axios.post('/api/pelicula/actualizar', me.qs.stringify({
                    pk: me.id,
                    titulo: me.titulo,
                    sinopsis: me.sinopsis,
                    resena: me.resena,
                    poster: me.poster,
                    fecha_estreno: me.fecha_estreno,
                }),{
                            headers: {
                                "X-CSRFToken": me.csrfToken
                            },
                            xsrfHeaderName: "X-CSRFToken",
                })
                .then(function (response) {
                    me.modal = 0;
                    me.listar();
                    if(me.imageData!=""){
                        me.subirPoster();
                    }
                    swal(
                        'Actualizado!',
                        'La pelicula ha sido actualizado.',
                        'success'
                    )
                })
                .catch(function (error) {
                    console.log(error);
                });
            },

            /**
                 * Method: subirPoster
                 * Description: Realiza una peticion al API REST a la url api/pelicula/subir_poster para actualizar el poster de una pelicula
                 * @param: poster  {string} base64
             */
            subirPoster(){
                let me = this;
                let formData = new FormData();
                formData.append('poster', me.imageData);
                formData.append('pk', me.id);
                axios.post( '/api/pelicula/subir_poster',
                        formData,
                        {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            "X-CSRFToken": me.csrfToken
                        },
                        xsrfHeaderName: "X-CSRFToken",
                      }
                ).then(function(){
                    console.log('SUCCESS!!');
                })
                .catch(function(){
                    console.log('FAILURE!!');
                });
            },

            /**
                 * Method: validar
                 * Description: Valida los parametros obligatorios del formulario de registro
             */
            validar(){
                this.error = 0;
                this.errors = [];
                if(!this.titulo) this.errors.push("El titulo no puede estar vacio");
                if(!this.sinopsis) this.errors.push("La sinopsis no puede estar vacia");
                if(!this.resena) this.errors.push("La reseña no puede estar vacia");

                if(this.errors.length) this.error=1;
                return this.error;
            },

            /**
                 * Method: abrirModal
                 * Description: Muestra el modal de Registro y Edicion de Peliculas
             */
            abrirModal(action, data=[]){
                this.error = 0;
                switch(action){
                    case "registrar":{
                        this.modal = 1;
                        this.titulo_modal = "Registrar Cliente";
                        this.id = 0;
                        this.titulo = "";
                        this.sinopsis = "";
                        this.resena = "";
                        this.poster = "";
                        this.fecha_estreno = "";
                        this.imageData = "";
                        this.active = 1;
                        this.action = 1;
                        break;
                    }
                    case "actualizar":{
                        this.modal = 1;
                        this.titulo_modal = "Actualizar Pelicula";
                        this.id = data.id;
                        this.titulo = data.titulo;
                        this.sinopsis = data.sinopsis;
                        this.resena = data.resena;
                        this.poster = data.poster;
                        this.imageData = data.poster;
                        this.fecha_estreno = data.fecha_estreno;
                        this.active = data.active;
                        this.action = 2;
                        break;
                    }
                }


            },

            /**
                 * Method: desactivar
                 * Description: Realiza una peticion al API REST a la url api/pelicula/desactivar para desactivar una pelicula
                 * @param: pk  {int}
             */
            desactivar(idR){
                let me = this;
                swal({
                    title: 'Esta seguro de desactivar?',
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, desactivar!',
                    cancelButtonText: 'No!'
                }).then((result) => {

                    if (result.value) {
                        axios.post('/api/pelicula/desactivar', me.qs.stringify({
                            pk: idR,
                        }),{
                            headers: {
                                "X-CSRFToken": me.csrfToken
                            },
                            xsrfHeaderName: "X-CSRFToken",
                        })
                        .then(function (response) {

                            me.listar();
                            swal(
                                'Desactivado!',
                                'La pelicula ha sido desactivada.',
                                'success'
                            )
                        })
                        .catch(function (error) {
                            console.log(error);
                        });

                    }
                })
            },

            /**
                 * Method: activar
                 * Description: Realiza una peticion al API REST a la url api/pelicula/activar para activar una pelicula
                 * @param: pk  {int}
             */
            activar(idR){
                let me = this;
                swal({
                    title: 'Esta seguro de activar?',
                    //text: "You won't be able to revert this!",
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, activar!',
                    cancelButtonText: 'No!'
                }).then((result) => {

                    if (result.value) {
                        axios.post('/api/pelicula/activar', me.qs.stringify({
                            pk: idR,
                        }),{
                            headers: {
                                "X-CSRFToken": me.csrfToken
                            },
                            xsrfHeaderName: "X-CSRFToken",
                        })
                        .then(function (response) {

                            me.listar();
                            swal(
                                'Activado!',
                                'La pelicula ha sido activada.',
                                'success'
                            )
                        })
                        .catch(function (error) {
                            console.log(error);
                        });

                    }
                })
            },

            /**
                 * Method: getCookie
                 * Description: Obtiene una cookie del navegador, se crea para obtener csrftoken
            */
            getCookie(name){
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            },
        },
        mounted() {
            console.log('Pelicula Component mounted.')
            console.log(this)
            this.qs = require('qs');
            this.csrftoken = this.getCookie('csrftoken');
            this.listar();
        },
    }
</script>

<style>
    .modal-content{
        width: 100% !important;
        position: absolute !important;
    }
    .mostrar{
        display: list-item !important;
        opacity: 1 !important;
        position: absolute !important;
        background-color: #3c29297a !important;
    }
    .div-error{
        display: flex;
        justify-content: center;
    }
    .text-error{
        color: red !important;
        font-weight: bold;
    }
    .file-upload-form, .image-preview {
        font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
        padding: 20px;
    }
    img.preview {
        max-width: 200px;
        max-height: 200px;
        background-color: white;
        border: 1px solid #DDD;
        padding: 5px;
    }
    img.preview-table{
        max-width: 60px;
        max-height: 60px;
        border: 2px solid #DDD;
        padding: 5px;
    }
</style>