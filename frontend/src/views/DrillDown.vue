<template>
  <div class="container main">
    <h1 class="is-size-2"> Device Drilldown </h1>
    <div v-for="device in devices" :key="device.id"> 
      <h3>{{ device.id }}</h3>
      <p><b>Lat:</b> {{ device.lat }} <b>Lon:</b> {{ device.lon }}</p>
      <line-chart :data="tsForDevice(key)" />
      <hr />
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
export default {
  data () { return {} },
  computed: {
    ...mapState(['devices']),
    ...mapGetters(['tsForDevice']),
    deviceKeys() { return Object.keys(this.devices) }
  },
  beforeMount() {
    this.$store.dispatch('loadAll')
  }
}
</script>
<style>
.container.main {
  margin-top: 2rem;
}
