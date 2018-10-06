<template>
  <div class="container">
    <h1 class="is-size-2"> Device Drilldown </h1>
    <div v-for="device in devices" :key="device.id"> 
      <h3>{{ device.name }}</h3>
      <p><b>Lat:</b> {{ device.lat }} <b>Lon:</b> {{ device.lon }}</p>
      <line-chart :data="tsForDevice(device.id)" />
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
    ...mapGetters(['tsForDevice'])
  },
  beforeMount() {
    this.$store.dispatch('loadAll')
  }
}
</script>
