<template>
  <div :style="{ height: height + 'px' }" class="header-img">
    <router-link to="/shout_voice_now">
      <v-btn elevation="2" x-large>叫ぶ</v-btn>
    </router-link>
  </div>
</template>
<script>
export default {
  data() {
    return {
      height: 0
    };
  },
  created() {
    if (process.client) {
      window.addEventListener("resize", this.handleResize);
      this.handleResize();
    }
  },
  destroyed() {
    if (process.client) {
      window.removeEventListener("resize", this.handleResize);
    }
  },
  methods: {
    handleResize() {
      this.height = window.innerHeight;
    }
  }
};
</script>

<style scoped>
.header-img {
  background-image: url(../img/home.jpg);
  background-color: #555555;
  /* display: block;
  margin-left: auto;
  margin-right: auto; */
}
</style>
