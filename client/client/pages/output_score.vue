<template>
  <div>
    <h1>声量の表示</h1>
    <router-link to="/start_shout">
      <v-btn elevation="2" x-large>スタート画面に戻る</v-btn>
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dat: []
    };
  },
  async mounted() {
    const url = "/api/scream_list/";
    const response = await this.$axios.get(url);
    this.dat = response.data;
    console.log(this.dat);
  }
};
</script>

<style>
* {
  background-color: #edeae2;
}
</style>
