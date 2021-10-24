<template>
  <div class="hero_3 overlay">
    <div class="text-box">
      <h1 class="title">あなたの熱量！！</h1>
      <p class="description_1">
        ○○点
      </p>
      <p class="description_2">
        SNSでシェアしよう！
      </p>
      <p class="description_3">
        <a href="https://ja-jp.facebook.com/">
          <img
            src="https://www.facebook.com/images/fb_icon_325x325.png"
            width="50"
            height="50"
          />
        </a>
        <a href="https://www.instagram.com/?hl=ja">
          <img
            src="https://play-lh.googleusercontent.com/h9jWMwqb-h9hjP4THqrJ50eIwPekjv7QPmTpA85gFQ10PjV02CoGAcYLLptqd19Sa1iJ"
            width="50"
            height="50"
          />
        </a>
        <a href="https://line.me/ja/">
          <img
            src="https://seeklogo.com/images/L/line-messenger-logo-F9E667D0A2-seeklogo.com.png"
            width="50"
            height="50"
          />
        </a>
      </p>
      <p class="description_4">
        <router-link to="/start_shout">
          <v-btn elevation="2" x-large>はじめに戻る</v-btn>
        </router-link>
      </p>
    </div>
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
/* 前提 */

body {
  margin: 0;
  padding: 0;
}

/* 全画面表示CSS */

.hero_3 {
  height: 100vh; /* 全画面表示 */
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  background-image: url(../img/319.jpg);
}

/* 黒の背景 */

.overlay::after {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  content: "";
  background: rgba(0, 0, 0, 0.4);
}

/* テキスト */

.text-box {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  z-index: 100;
}
.title {
  font-family: Roboto;
  font-size: 60px;
  font-weight: bold;
  line-height: 1.2;
  padding: 0 50px;
  text-align: center;
  color: #fff;
}
.description_1 {
  font-size: 24px;
  color: white;
  text-align: center;
}
.description_2 {
  margin-top: 10px;
  font-family: Roboto;
  font-size: 32px;
  font-weight: bold;
  line-height: 1.2;
  padding: 0 50px;
  text-align: center;
  color: #fff;
}
.description_3 {
  color: white;
  text-align: center;
  padding: 20px;
}
.description_4 {
  color: white;
  text-align: center;
}
</style>
