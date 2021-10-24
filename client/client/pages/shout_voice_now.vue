<template>
  <div>
    <h1>声を出す瞬間</h1>
    <v-btn
      @click="startRecording"
      v-if="status == 'ready'"
      elevation="2"
      x-large
      >録音を開始する</v-btn
    >
    <v-btn
      v-if="status == 'recording'"
      @click="stopRecording"
      elevation="2"
      x-large
      >録音を停止する</v-btn
    >
    <router-link to="/output_score">
      <v-btn elevation="2" x-large>
        出し終えたらスコアを出力する画面に映る
      </v-btn>
    </router-link>
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
      this.status = "ready";
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
        const api_url = "/api/scream_upload/";
        console.log("api_url")
        console.log(api_url)
        console.log("a")
        console.log(a)
        console.log(a.href)
        // const file = new File([a], a.download, {type: "application/octet-stream"});
        // const response = this.$axios.post(api_url, {"audio_path":file});
        const response = this.$axios.post(api_url, {"audio_path":a});
        // const response = this.$axios.post(api_url, {"audio_path":a});
        // const response = this.$axios.post(api_url, {"audio_path":a.href});
        // const response = this.$axios.post(api_url, {"audio_path":a.download});
        console.log(response.data);
      });
      this.status = "ready";
    });
  }
});
</script>

<style>
* {
  background-color: #edeae2;
}
</style>
