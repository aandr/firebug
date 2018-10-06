<template>
  <div>
    <GmapMap :center="{lat:37.3863, lng:-122.0669}"
        :zoom="15"
        map-type-id="terrain"
        style="width: 100%; height: 800px"
        :options="{disableDefaultUI: true}"
        
    >
      <GmapMarker 
        v-for="device in devices"
        :key="device.id"
        :position="{lat: device.lat, lng: device.lng}"
        :options="google && {
           icon: {
            path: google.maps.SymbolPath.CIRCLE,
            strokeWeight: 7,
            scale: 10,
            strokeColor: 'red'
          },
        }"
        />
    </GmapMap>
    <div class="container">
    <div class="columns time-travel">
      <div class="column is-one-fifth is-size-5 label">
        Time travel
      </div>
      <div class="column is-four-fifths">  
        <vue-slide-bar :data="timeScale" :range="timeLabels" :value="1"/>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { gmapApi } from "vue2-google-maps";

export default {
  data() {
    return {};
  },
  computed: {
    google: gmapApi,
    ...mapState(["devices", "timeScale"]),
    timeLabels() {
      let n = 0
      this.timeScale.forEach(t => { 
        n += 1
        return { label: t.toLocaleString(), isHidden: n % 6 == 0}
      })
    }
  },
  beforeMount() {
    this.$store.dispatch('loadAll')
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
</style>