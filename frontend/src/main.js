import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import Chart from 'chart.js';
import Leaflet from 'leaflet';
import Vue from 'vue';
import VueChartkick from 'vue-chartkick';
import App from './App.vue';
import Navbar from './components/Navbar.vue';
import router from './router';
import store from './store';


delete Leaflet.Icon.Default.prototype._getIconUrl;


Leaflet.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

Vue.config.productionTip = false


Vue.use(Buefy)
Vue.use(VueChartkick, {adapter: Chart})
Vue.component('Navbar', Navbar)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
