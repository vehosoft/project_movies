
/**

 * @author   Francisco Rodriguez <frodriguez@vehosoft.com>

 * History

 * v1.0 – APP VUE JS para la administracion del Sitio Web

 * ----

*/

//Activar devtools para debugin en navegador
Vue.config.devtools = true;

new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  components: { },
  data: {
    menu: 0,
    title: 'Sitio de peliculas y reseñas',
    email:'',
    password:'',
    comentario: '',
    nombre_usuario:'',
    array: [],
    preview_rec: {},
    modal:0,
    errors:[],
    error: false,
    pagination:{
        'total': 0,
        'current_page': 1,
        'per_page':  0,
        'last_page':  1,
        'from':  0,
        'to':  0,
    },
    offset: 3,
    show_preview: 0,
    csrftoken: '',
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
             * Method: login
             * Description: Realiza una peticion al API REST a la url api/login para la autenticacion del usuario
             * @param: email  {string}
             * @param: password  {string}
         */
        login(){
            let me = this
            let data = new FormData();
            data.append('email', me.email);
            data.append('password', me.password);
            axios.post('api/login',data,{
                        headers: {
                            "X-CSRFToken": me.csrfToken
                        },
                        xsrfHeaderName: "X-CSRFToken",
            })
            .then(function (response) {
                console.log(response);
                if(response.data.success){
                    location.reload();
                }else{
                    swal(
                        'Error!',
                        'Datos de acceso incorrectos',
                        'error'
                    )
                }

            })
            .catch(function (error) {
                console.log(error);
            });

        },

        /**
             * Method: modal_registro
             * Description: Muestra el modal de Registro de usuario
         */
        modal_registro(){
            this.error = 0;
            this.errors = [];
            this.email = '';
            this.password = '';
            this.modal=1;
        },

        /**
             * Method: registrar
             * Description: Realiza una peticion al API REST a la url api/registro para registrar un usuario
             * @param: nombre  {string}
             * @param: email  {string}
             * @param: password  {string}
         */
        registrar(){
            let me = this
            if(this.validar()){
                return;
            }
            let data = new FormData();
            data.append('nombre', me.nombre_usuario);
            data.append('email', me.email);
            data.append('password', me.password);
            axios.post('api/registro',data,{
                        headers: {
                            "X-CSRFToken": me.csrfToken
                        },
                        xsrfHeaderName: "X-CSRFToken",
            })
            .then(function (response) {
                console.log(response);
                if(response.data.success){
                    me.login();
                }else{
                    swal(
                        'Error!',
                        'Datos de registro incorrectos',
                        'error'
                    )
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        },

        /**
             * Method: listar
             * Description: Realiza una peticion al API REST a la url api/pelicula/lista para obtener una lista de peliculas
             * @param: page  {int}
             * @param: per_page  {int}
             * @param: orderby  {string}
         */
        listar(page=false){
            let me=this;
            if(page) me.pagination.current_page = page;
            var url = '/api/pelicula/lista?page='+me.pagination.current_page+'&per_page=12&orderby=fecha_estreno';
            axios.get(url)
            .then(function (response) {
                console.log(response);
                var resp = response.data;
                me.array = resp.records;
                me.pagination = resp.pagination;
            })
            .catch(function (error) {
                console.log(error);
            });
        },

        /**
             * Method: preview
             * Description: Realiza una peticion al API REST a la url api/pelicula/detalle para obtener un registro de pelicula
             * @param: pk  {int}
         */
        preview(idP){
            let me = this
            var url = 'api/pelicula/detalle?pk='+idP;
            axios.get(url,{
                        headers: {
                            "X-CSRFToken": me.csrfToken
                        },
                        xsrfHeaderName: "X-CSRFToken",
            })
            .then(function (response) {
                console.log(response);
                var rec = response.data.record;
                me.preview_rec = rec;
                me.show_preview = 1
            })
            .catch(function (error) {
                console.log(error);
            });
        },

        /**
             * Method: save_comentario
             * Description: Realiza una peticion al API REST a la url api/pelicula/comentario para registrar un comentario de pelicula
             * @param: pelicula_id  {int}
             * @param: comentario  {string}
         */
        save_comentario(pelicula_id,comentario){
            let me = this
            let data = new FormData();
            data.append('pelicula_id', pelicula_id);
            data.append('comentario', comentario);
            axios.post('api/pelicula/comentario',data,{
                        headers: {
                            "X-CSRFToken": me.csrfToken
                        },
                        xsrfHeaderName: "X-CSRFToken",
            })
            .then(function (response) {
                console.log(response);
                swal(
                    'Comentario registrado',
                    'Gracias por contribuir, tu opinion es muy importante!',
                    'success'
                )
                me.comentario = '';
                me.preview(pelicula_id);
            })
            .catch(function (error) {
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
             * Method: validar
             * Description: Valida los parametros obligatorios del formulario de registro
         */
        validar(){
            this.error = 0;
            this.errors = [];
            if(!this.nombre_usuario) this.errors.push("El nombre no puede estar vacio");
            if(!this.email) this.errors.push("El email no puede estar vacio");
            if(!this.password) this.errors.push("El password no puede estar vacio");

            if(this.errors.length) this.error=1;
            return this.error;
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
       console.log('App site mounted.')
       this.csrftoken = this.getCookie('csrftoken');
       this.listar();
    }

});