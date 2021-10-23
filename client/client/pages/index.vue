<template>
  <div>
    <ul>
      <li v-for="(post, index) in posts" :key="index">
        <a :href="'post.url'" target="_blank" rel="noopener noreferrer">{{ post.title }}</a>
        <!-- <VueTagCloud v-bind:data="tagData"></VueTagCloud> -->
      </li>
    </ul>
  </div>
</template>

<script>
// import Vue from 'vue'
// import VueTagCloud from 'vue-tag-cloud'

// Vue({
//   el: '#app',
//   components: {
//     VueTagCloud
//   }
// })

export default {
  async asyncData ({ $axios }) {
    // 取得先のURL
    const url = 'https://qiita.com/api/v2/items'
    // リクエスト（Get）
    const response = await $axios.$get(url)
    // 配列で返ってくるのでJSONにして返却
    return {
      posts: response
    }
  }
}
</script>

<style>
* {
  background-color: #EDEAE2;
}
</style>
