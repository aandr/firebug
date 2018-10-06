import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import Chart from 'chart.js';
import Vue from 'vue';
import VueChartkick from 'vue-chartkick';
import App from './App.vue';
import Navbar from './components/Navbar.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false


Vue.use(Buefy)
Vue.use(VueChartkick, {adapter: Chart})
Vue.component('Navbar', Navbar)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
