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
  </div>
</template>

<script>
import { mapState } from "vuex";
import {gmapApi} from 'vue2-google-maps'

export default {
  data() {
    return {
    }
  },
  computed: {
    google: gmapApi,
    ...mapState(["devices"])
  }
};
</script>

