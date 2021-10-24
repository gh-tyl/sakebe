<template>
  <div class="hero overlay">
    <div class="text-box">
      <h1 class="title">SAKEBE</h1>
      <p class="description_1">
        さぁ！MIYASITA PARKで「渋谷の町」に向けて叫ぼう！
      </p>
      <p class="description_2">
        <router-link to="/shout_voice_now">
          <v-btn elevation="2" x-large>叫ぶ</v-btn>
        </router-link>
      </p>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style scoped>
/* 前提 */

body {
  margin: 0;
  padding: 0;
}

/* 全画面表示CSS */

.hero {
  height: 100vh; /* 全画面表示 */
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  background-image: url(https://t4.ftcdn.net/jpg/00/16/11/59/360_F_16115921_mPioYHrQ3WRFVp24Az125VTVa7364vkg.jpg);
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
.description_1,
.description_2 {
  color: white;
  text-align: center;
}
</style>
