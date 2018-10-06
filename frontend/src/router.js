import Vue from 'vue';
import Router from 'vue-router';
import DrillDown from './views/DrillDown.vue';
import Home from './views/Home.vue';
import MapView from './views/MapView.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/drilldown',
      name: 'Drilldown',
      component: DrillDown
    },
    {
      path: '/map',
      name: 'Map',
      component: MapView
    },
  ]
})
