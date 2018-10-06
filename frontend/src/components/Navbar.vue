<template>
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="container">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="../assets/logo.png" height="45">
      </a>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">
          Home
        </router-link>

        <router-link class="navbar-item" to="/map">
          Map
        </router-link>

        <router-link class="navbar-item" to="/alert-log">
          Alert Log
        </router-link>

        <router-link class="navbar-item" to="/drilldown">
          Drilldown
        </router-link>
      </div>
    </div>
  </div>
</nav>
</template>

<style>
.navbar {
  border-bottom: 1px solid #ccc
}
</style>
