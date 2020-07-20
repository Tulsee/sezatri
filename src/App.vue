<template>
  <div id="app">
    <!-- Page Preloder -->
    <div id="preloder">
      <div class="loader"></div>
    </div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>
<script>
import Navbar from "./components/shared/Navbar";
import Footer from "./components/shared/Footer";
export default {
  name: "App",
  components: { Navbar, Footer }
};
</script>
<style lang="scss">
</style>
