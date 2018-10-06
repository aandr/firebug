<template>
  <div>
    <l-map ref="map" :zoom=13 :center="[37.3863, -122.0669]">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker 
        v-for="device in devices"
        :key="device.id"
        :lat-lng="[device.lat, device.lng]" />
    </l-map>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
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

