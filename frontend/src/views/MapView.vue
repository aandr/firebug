<template>
  <div>
    <l-map ref="map" :zoom=13 :center="[37.3863, -122.0669]" style="width: 100%; height: 80%">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker 
        v-for="device in devices"
        :key="device.id"
        :lat-lng="[device.lat, device.lon]" />
    </l-map>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

export default {
  components: { LMap, LTileLayer, LMarker },
  data() {
    return {
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    };
  },
  computed: {
    ...mapState(["devices"])
  }
};
</script>

