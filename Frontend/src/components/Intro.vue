<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1"
        ><span class="tooltip">t-SNE 알고리즘<span class="tooltiptext tooltip-top"
            >t-SNE이란 고차원 공간상의 데이터를 2차원 공간으로 가져와 시각화하는
            비선형 차원 축소 기법</span></span>으로 시각화된 학교들의 관계를 살펴보세요 !</span
      >
      <span class="intro_msg2"
        >∙ 점을 누르면 해당 학교의 자세한 페이지로 이동합니다.<br />
        ∙ 대륙 이름을 누르면 해당 대륙은 제외됩니다 !</span
      >
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      sampleData: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
<style scoped>
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-top: 7%;
  margin-left: 10%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 1440px;
  height: 58px;
  font-family: Inter;
  text-align: left;
  font-size: 44.86062240600586px;
  margin-top: 10px;
  letter-spacing: 0;
  display: flex;
}
.intro_msg2 {
  color: rgba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 745px;
  height: 43px;
  font-family: Inter;
  text-align: left;
  margin-top: 10px;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
.tooltip {
  position: relative;
  display: block;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 200px;
  background-color: white;
  color: black;
  text-align: center;
  border-radius: 6px;
  padding: 15px;
  font-size: 15px;
  border: 1px solid black;
  position: absolute;
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
.tooltip .tooltiptext::after {
  content: ' ';
  position: absolute;
  border-style: solid;
  border-width: 5px;
}
.tooltip .tooltip-top {
  width: 285px;
  bottom: 110%;
  left: 25%;
  margin-left: -60px;
}

.tooltip .tooltip-top::after {
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-color: black transparent transparent transparent;
}
</style>