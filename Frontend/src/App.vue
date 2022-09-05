<template >
  <Header></Header>
  <intro v-if="$route.path.includes('plot')"></intro>
  <router-view class="wrapbox"></router-view>
  <Footer class="footer" v-if="!$route.path.includes('detailresult')"></Footer>
</template>
<script>
import Header from './components/HeaderComp.vue'
import Footer from './components/FooterComp.vue'
import Intro from './components/Intro.vue'
export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Intro
  },
  methods: {}
}
</script>

<style scoped>
* {
  font-family: Inter;
}
.wrapbox {
  min-height: 100%;
  height: auto;
  padding-bottom: 180px;
}
.footer {
  position: relative;
  transform: translatY(-100%);
  margin-bottom: 30px;
}
#app {
  display: flex;
  flex-direction: column;
}
#html {
  height: 100%;
}
#body {
  height: 100%;
}
</style>
