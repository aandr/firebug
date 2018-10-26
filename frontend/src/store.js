import axios from 'axios';
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    devices: {},
    currentTime: 0,
    cursors: {},
    timeScale: []
  },
  getters: {
    tsForDevice: (state) => (deviceId) => {
      const device = state.devices[deviceId]
      device.ts.map((val, i) => [val, device.concentration[i]])
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
      if (typeof time == 'number') {
        time = new Date(time)
      }
      state.currentTime = time
      Object.keys(state.devices).forEach(id =>
        state.cursors[id] = state.devices[id].ts.findIndex(n => n >= time)
      )
    },
    updateDevices(state, data) {
      state.devices = data
      Object.keys(data).forEach(key => state.cursors[key] = 0)
    },
    setTimeRange(state, range) {
      const out = []
      const minTime = range[0]
      const maxTime = range[1]
      let current = minTime
      while (current < maxTime) {
        out.push(current)
        current = new Date(current.getTime() + 1 * 60000)
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
            const ts = device['time_series']['timelist'].map(n => new Date(n + " UTC"))
            minTime = minTime > ts[0] ? ts[0] : minTime
            maxTime = maxTime < ts[ts.length - 1] ? ts[ts.length - 1] : maxTime
            devices[device['device_number']] = {
              id: device['device_number'],
              ts: ts,
              concentration: device['concentration_series']['concentrationlist'],
              lat: device['geolocation']['latitude'],
              lon: device['geolocation']['longitude']
            }
          })

          commit('updateDevices', devices)
          commit('setTimeRange', [minTime, maxTime])
        })
    },
  }
})
