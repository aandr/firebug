import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import Chart from 'chart.js';
import Vue from 'vue';
import VueChartkick from 'vue-chartkick';
import VueSlideBar from 'vue-slide-bar';
import * as VueGoogleMaps from 'vue2-google-maps';
import App from './App.vue';
import Navbar from './components/Navbar.vue';
import router from './router';
import store from './store';


Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDA3I5P_b18f2Sqis8BmIdLERnvBWCPxD0',
    libraries: '', // This is required if you use the Autocomplete plugin
  },
  installComponents: true,
})


Vue.component('vue-slide-bar', VueSlideBar)
Vue.config.productionTip = false
Vue.use(Buefy)
Vue.use(VueChartkick, {adapter: Chart})
Vue.component('Navbar', Navbar)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
