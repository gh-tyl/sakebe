<template>
  <div>
    <ul>
      <li v-for="(post, index) in posts" :key="index">
        <!-- <span id="content" :style="{top: Math.floor(Math.random() * 500) + 'px', left: Math.floor(Math.random() * 500) + 'px', color: fontColorSelector(post.color), 'font-size': fontSizeSelector(post.decibel) + 'px'}"> -->
        <span id="content" :style="{top: Math.floor(Math.random() * 500) + 'px', left: Math.floor(Math.random() * 500) + 'px', color: fontColorSelector(post.color), 'font-size': post.decibel*3 + 'px'}">
          <client-only>
            <div id="textcontent">
              {{ post.content }} <!-- contentにする -->
            </div>
          </client-only>
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  // async asyncData ({ $axios }) {
  //   // 取得先のURL
  //   // const url = 'https://qiita.com/api/v2/items'
  //   const url = '/api/scream_upload/'
  //   // リクエスト（Get）
  //   const response = await $axios.$get(url);
  //   // 配列で返ってくるのでJSONにして返却
  //   return {
  //     posts: response
  //   };
  // },

  data() {
    return {
      color: [],
      posts: []
    }
  },
  async mounted() {
    const url = "/api/scream_list/";
    const response = await this.$axios.get(url);
    this.dat = response.data;
    console.log(this.dat['results'])
    this.posts = this.dat['results']
  },  
  // computed: {
  //   // a computed getter
  //   fontColor: function () {
  //     this.response.likes_count
  //     if (response == 0){
  //       this.color[0] = "red"
  //     }
  //     return "red"
  //   }
  // },
  methods: {
    fontColorSelector: function (likes_count) {
      if (likes_count == 0){
        return "#8BAAD3"
      }
      return "#AFA0CD"
    },
    fontSizeSelector: function (decibel) {
      if (decibel > 0 && decibel < 100 ){
        return "30"
      }
      return "50"
    }
  }
  // data: {
  //   color: [],
  // },
  // computed: {
  //   let response = this.response.likes_count
  //   if (response == 0){
  //     this.color[0] = "red"
  //   }
  // }
}
</script>

<style>
* {
  background-color: #EDEAE2;
}

#content {
  position: relative;
  width: 100%;
  /* height: 400px; */
  margin: 0 auto;
  overflow: hidden;
}

span {
  min-height: 200px;
  background-color: transparent;
}

#textcontent {
  min-height: 70px;
  background-color: transparent;
}
</style>
