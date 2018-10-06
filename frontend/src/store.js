import axios from 'axios';
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    devices: [
      { 'id': '200040001047373333353132', 'name': 'Sensor 1', lat: 37.3863, lng: -122.0769 },
      {'id': '35005c000d51363034323832', 'name': 'Sensor 2',  lat: 37.3763, lng: -122.0669 },
      {'id': '2d0049000d51363034323832', 'name': 'Sensor 3',  lat: 37.3963, lng: -122.0569 }
    ],
    ts: [],
    currentTime: 0,
  },
  getters: {
    tsForDevice: (state) => (deviceId) => {
      let out = {}
      console.log(state.ts)
      return state.ts.filter(n => n[1] == deviceId).map(n => [n[0], n[3]])
    }

  },
  mutations: {
    setTime(time) {
      this.currentTime = time
    },
    setTs(state, ts) {
      state.ts = ts
    }
  },
  actions: {
    loadAll({commit}) {
      axios.get("http://fbug-store.herokuapp.com/csv")
        .then(result => {
          const rows = result.data.split("\n")
          rows.shift()
          const ts = rows.map(row => row.trim().split(","))
          commit('setTs', ts)
          commit('setTime', ts[0][0])
        })
    },
  }
})
