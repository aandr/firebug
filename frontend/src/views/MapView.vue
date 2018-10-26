<template>
  <div>
    <GmapMap :center="{lat:37.3863, lng:-122.0669}"
        :zoom="19"
        map-type-id="terrain"
        style="width: 100%; height: 500px"
        :options="{disableDefaultUI: true}"
        ref="map"
    />
    <div cl5ss="container">
    <div class="columns time-travel">
      <div class="column is-one-fifth is-size-5 label">
        Time travel
      </div>
      <div class="column is-four-fifths">  
        <vue-slide-bar :value="currentTimeNumber" @input="setTime" :data="timeScaleNumbers">
          <template slot="tooltip" slot-scope="tooltip">
            <div class="vue-slide-bar-tooltip">
              {{cleanTimeValue}}
            </div>
          </template>
        </vue-slide-bar>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
//        :position="{lat: device.lat, lng: device.lon}"
import { mapState, mapMutations } from "vuex";
import { gmapApi } from "vue2-google-maps";
import * as d3 from 'd3'

export default {
  data() {
    return {
      markerHandles: {}
    }
  },
  computed: {
    cleanTimeValue () { 
      const date = new Date(this.currentTime)
      return date.getHours() + ":" + date.getMinutes().toString().padStart(2, '0')
    },
    currentTimeNumber() { return this.currentTime ? this.currentTime.getTime() : 0 },
    google: gmapApi,
    ...mapState(["devices", "timeScale", "currentTime", "cursors"]),
    timeLabels() {
      let n = 0
      this.timeScale.forEach(t => { 
        n += 1
        let item = { label: t.toLocaleString() }
        if (n % 6 == 0) item.isHidden = true
        return item
      })
    },
    timeScaleNumbers() {
      return this.timeScale.map(n => n.getTime())
    }
  },
  methods: {
    ...mapMutations(['setTime'])
  },
  watch: {
    currentTimeNumber: { 
      handler (newValue) {
        const google = gmapApi()
        var colorScale = d3.scaleLinear().domain([0, 4000, 5000]).range(['green', 'yellow', 'red']);


        this.$refs.map.$mapPromise.then(map => {
          Object.keys(this.devices).forEach(key => {
            const device = this.devices[key]

            const targetColor = colorScale(device.concentration[this.cursors[device.id]])
            const icon = {
                  path: google.maps.SymbolPath.CIRCLE,
                  strokeWeight: 7,
                  scale: 15 ,
                  strokeColor: targetColor
                }
            if (!(key in this.markerHandles)) {
              const marker =  new google.maps.Marker({
                position: {lat: device.lat, lng: device.lon},
                icon: icon
              })
              this.markerHandles[key] = marker
              marker.setMap(map)
            } else {
              this.markerHandles[key].set('icon', icon)
            }
          })
        })
      }
    }
  },
  beforeMount() {
    const this$1 = this
    this.$store.dispatch('loadAll')
  },
  mounted() {
    const this$1 = this
    setInterval(function() {
      if (this$1.currentTimeNumber) {
        this$1.setTime(this$1.currentTimeNumber + 60000)
        console.log("time")
      }
    }, 500)
  }
};
</script>


<style>
.time-travel {
  background: #f0f0f0;
  margin: 1rem;
  padding: 0.5rem;
  align-items: flex-end;
}

.vue-slide-bar-tooltip {
  width: 6em;
  top: -10px;
}
.tooltip {
  background: #1066FD;
  top: -15px;
  color: white;
  padding: 5px;
  border-radius: 5px;
}
</style>