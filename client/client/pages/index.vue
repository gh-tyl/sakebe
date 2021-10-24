<template>
  <div>
    <ul>
      <li v-for="(post, index) in posts" :key="index">
        <span id="content" :style="{top: Math.floor(Math.random() * 500) + 'px', left: Math.floor(Math.random() * 500) + 'px', color: fontColorSelector(post.likes_count)}">
          <client-only>
            <div id="textcontent">
              {{ post.title }} <!-- contentにする -->
            </div>
          </client-only>
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  async asyncData ({ $axios }) {
    // 取得先のURL
    const url = 'https://qiita.com/api/v2/items'
    // リクエスト（Get）
    const response = await $axios.$get(url);
    // 配列で返ってくるのでJSONにして返却
    return {
      posts: response
    };
  },
   data: {
    color: []
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
