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
    devices: {},
    currentTime: 0,
    cursors: {},
    timeScale: []
  },
  getters: {
    tsForDevice: (state) => (deviceId) => {
      let out = {}
      console.log(state.ts)
      return state.ts.filter(n => n[1] == deviceId).map(n => [n[0], n[3]])
    },
    snapshot: (state) => {
      const out = {}
      Object.keys(state.devices).forEach(key => {
        const cursor = state.cursors[key]
        out[key] = state.devices[key].concentration[cursor]
      })
      return out
    }
  },
  mutations: {
    setTime(state, time) {
      state.currentTime = time
      Object.keys(state.devices).forEach(id =>
        state.cursor[id] = state.devices[id].ts.findIndex(n => n >= time)
      )
    },
    updateDevices(state, data) {
      state.data = data
      Object.keys(data).forEach(key => state.cursors[key] = 0)
    },
    setTimeRange(state, range) {
      const out = []
      const minTime = range[0]
      const maxTime = range[1]
      let current = minTime
      while (current < maxTime) {
        out.push(current)
        current = new Date(current.getTime() + 10 * 60000)
      }
      state.timeScale = out
    }
  },
  actions: {
    loadAll({commit}) {
      axios.get("http://fbug-data.herokuapp.com/firebug/get_all_devices")
        .then(({data}) => {
          const devices = {}
          let minTime = new Date('2030-1-1')
          let maxTime = new Date(0)

          data['devices'].forEach(device => {
            const ts = device['time_series']['timelist'].map(n => new Date(n))
            minTime = minTime > ts[0] ? ts[0] : minTime
            maxTime = maxTime < ts[ts.length - 1] ? ts[ts.length - 1] : maxTime
            devices[device['device_number']] = {
              ts: ts,
              concentration: device['concentration_series']['concentrationlist'],
              location: device['geolocation']
            }
          })

          commit('updateDevices', devices)
          commit('setTimeRange', [minTime, maxTime])
        })
    },
  }
})
