<template>
  <div class="hero_2 overlay">
    <div class="text-box">
      <h1 class="title">あなたの「今の気持ち」をSAKEBE！！</h1>
      <p class="description_1">
        <v-btn
          @click="startRecording"
          v-if="status == 'ready'"
          elevation="2"
          x-large
          >叫ぶ</v-btn
        >
        <v-btn
          v-if="status == 'recording'"
          @click="stopRecording"
          elevation="2"
          x-large
          >叫けび終わったらクリック！</v-btn
        >
        <router-link to="/output_score">
          <v-btn elevation="2" x-large v-if="status == 'next'">
            あなたの熱意をチェックしよう！
          </v-btn>
        </router-link>
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  data: function() {
    return {
      // ① 変数を宣言する部分
      status: "init", // 状況
      recorder: null, // 音声にアクセスする "MediaRecorder" のインスタンス
      audioData: [], // 入力された音声データ
      audioExtension: "" // 音声ファイルの拡張子
    };
  },
  methods: {
    startRecording() {
      this.status = "recording";
      this.audioData = [];
      this.recorder.start();
      console.log(this.status);
    },
    stopRecording() {
      this.recorder.stop();
      this.status = "next";
    },
    getExtension(audioType) {
      let extension = "wav";
      const matches = audioType.match(/audio\/([^;]+)/);

      if (matches) {
        extension = matches[1];
      }

      return "." + extension;
    }
  },
  mounted() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
      this.recorder = new MediaRecorder(stream);
      this.recorder.addEventListener("dataavailable", e => {
        this.audioData.push(e.data);
        this.audioExtension = this.getExtension(e.data.type);
      });
      this.recorder.addEventListener("stop", () => {
        const audioBlob = new Blob(this.audioData);
        const url = URL.createObjectURL(audioBlob);
        let a = document.createElement("a");
        a.href = url;
        a.download = Math.floor(Date.now() / 1000) + this.audioExtension;
        document.body.appendChild(a);
        a.click();
      });
      this.status = "ready";
    });
  }
});
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

/* 全画面表示CSS */

.hero_2 {
  height: 100vh; /* 全画面表示 */
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  background-image: url(https://previews.123rf.com/images/badmanproduction/badmanproduction1208/badmanproduction120800048/14658040-%E4%BA%BA%E3%81%AE%E5%88%86%E9%9B%A2%E3%81%AB%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88%E3%82%92%E5%8F%AB%E3%81%B6.jpg);
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
  color: white;
  text-align: center;
}
</style>
