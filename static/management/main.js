
/**

 * @author   Francisco Rodriguez <frodriguez@vehosoft.com>

 * History

 * v1.0 – APP VUE JS para el Panel de Administracion

 * ----

*/

Vue.config.devtools = true;
import UploadImage from 'vue-upload-image';
import pelicula from './components/Pelicula.vue'
const app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  components: { pelicula,UploadImage },
  data: {
    menu: 0,
    title: 'Panel de administracion para peliculas y reseñas'
  }
});