<template>
<div class="grid-container">
  <div
      v-for="(src, index) in image_list"
      :key="index"
      class="pic"
      @click="() => showImg(index)"
    >
    <div>{{ src.title }}</div><div ><img :src="src.src"></div>
  </div>
  <vue-easy-lightbox
    :visible="visible"
    :imgs="image_list"
    :index="index"
    @hide="handleHide"
  ></vue-easy-lightbox>
</div>
</template>

<script>
import VueEasyLightbox from 'vue-easy-lightbox'

export default {
  components: {
    VueEasyLightbox
  },
  name: "caipirinha-visualization-images",
  props: ["visualizationData"],
  data: function() {
    return {
      html: this.visualizationData.html,
      image_list: this.visualizationData.image_list,
      visible: false,
      index: 0   // default: 0
    }
  },
  methods: {
    showSingle() {
      this.show()
    },
    showMultiple() {
      this.index = 1  // index of imgList
      this.show()
    },
    showImg (index) {
        this.index = index
        this.visible = true
    },
    handleHide() {
      this.visible = false
    }
  }
};
</script>

<style lang="scss" scoped>

.grid-container {
    display: flex;
    flex-flow: wrap;
}

img {
  /* -webkit-filter: blur(8px);  Safari 6.0 - 9.0 */
  /* filter: blur(8px); */
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 200px;
}
</style>