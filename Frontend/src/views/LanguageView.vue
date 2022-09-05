<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1">선호하는 언어를 알려주세요!</span>
      <span class="intro_msg2">중복 선택이 가능합니다.</span>
    </div>
    <div class="boxwrapper">
      <div class="box">
        <div class="box_item">
          <label class="label">
            <input
              style="zoom: 2"
              type="checkbox"
              value="english"
              v-model="language"
            />&nbsp;영어</label
          >
        </div>
        <div class="box_item">
          <label class="label">
            <input
              style="zoom: 2"
              type="checkbox"
              value="spanish"
              v-model="language"
            />&nbsp;스페인어</label
          >
        </div>
        <div class="box_item">
          <label class="label">
            <input
              style="zoom: 2"
              type="checkbox"
              value="german"
              v-model="language"
            />&nbsp;독일어</label
          >
        </div>
        <div class="box_item">
          <label class="label">
            <input
              style="zoom: 2"
              type="checkbox"
              value="japanese"
              v-model="language"
            />&nbsp;일본어</label
          >
        </div>
        <div class="box_item">
          <label class="label">
            <input
              style="zoom: 2"
              type="checkbox"
              value="chinese"
              v-model="language"
            />&nbsp;중국어</label
          >
        </div>
      </div>
    </div>
    <button @click="next" :disabled="language.length === 0" :class="{ blackbox: language.length > 0, graybox: language.length === 0}">
      선택 완료
    </button></div>
</template>
<script>
export default {
  components: {},
  props: {},
  data() {
    return {
      case: [],
      language: []
    }
  },
  setup() {},
  create() {},
  mounted() {
    this.case = JSON.parse(sessionStorage.getItem('case'))
  },
  unmounted() {},
  methods: {
    next() {
      sessionStorage.setItem('language', JSON.stringify(this.language))
      this.$router.push('result')
      sessionStorage.setItem('recommended', 'false')
    }
  }
}
</script>
<style scoped>
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 600px;
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  margin-left: 10%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 840px;
  height: 58px;
  font-family: Inter;
  text-align: left;
  font-size: 44.86062240600586px;
  letter-spacing: 0;
}

.intro_msg2 {
  color: rgba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 745px;
  height: 43px;
  font-family: Inter;
  text-align: left;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
.boxwrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 5%;
}
.box {
  box-shadow: 0px 54.361366271972656px 54.361366271972656px
    rgba(0, 0, 0, 0.10000000149011612);
  background-color: rgba(255, 255, 255, 0.699999988079071);
  width: 332.96337890625px;
  height: 366.939208984375px;
  border-top-left-radius: 27.180683135986328px;
  border-top-right-radius: 27.180683135986328px;
  border-bottom-left-radius: 27.180683135986328px;
  border-bottom-right-radius: 27.180683135986328px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.label {
  margin-left: 5%;
  color: #616161;
  width: 278.60198974609375px;
  height: 41px;
  text-align: left;
  font-size: 27.180683135986328px;
  letter-spacing: 0;
}
.check {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 200px;
  height: 58px;
  position: absolute;
  left: 640px;
  top: 935px;
  border-top-left-radius: 30.988557815551758px;
  border-top-right-radius: 30.988557815551758px;
  border-bottom-left-radius: 30.988557815551758px;
  border-bottom-right-radius: 30.988557815551758px;
}
.check_1 {
  background-color: gray;
  width: 200px;
  height: 58px;
  position: absolute;
  left: 640px;
  top: 935px;
  border-top-left-radius: 30.988557815551758px;
  border-top-right-radius: 30.988557815551758px;
  border-bottom-left-radius: 30.988557815551758px;
  border-bottom-right-radius: 30.988557815551758px;
}

.check_2 {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  border: 0;
  color: rgba(255, 255, 255, 1);
  width: 220px;
  height: 42px;
  position: absolute;
  left: 659.5px;
  top: 943px;
  font-family: Inter;
  text-align: center;
  font-size: 28px;
  letter-spacing: 1;
  line-height: 42px;
}
.check_2_1 {
  background-color: gray;
  border: 0;
  color: rgba(255, 255, 255, 1);
  width: 220px;
  height: 42px;
  position: absolute;
  left: 659.5px;
  top: 943px;
  font-family: Inter;
  text-align: center;
  font-size: 28px;
  letter-spacing: 1;
  line-height: 42px;
}
a {
  text-decoration-line: none;
}
.blackbox {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 230px;
  height: 64.79875946044922px;
  position: absolute;
  left: 605px;
  top: 900px;
  border-top-left-radius: 21.362228393554688px;
  border-top-right-radius: 21.362228393554688px;
  border-bottom-left-radius: 21.362228393554688px;
  border-bottom-right-radius: 21.362228393554688px;
  font-size: 25px;
  font-weight: bold;
  color: white;
  border: 0;
  outline: 0;
}
.graybox {
  color: gray;
  width: 230px;
  height: 64.79875946044922px;
  position: absolute;
  left: 605px;
  top: 900px;
  border-top-left-radius: 21.362228393554688px;
  border-top-right-radius: 21.362228393554688px;
  border-bottom-left-radius: 21.362228393554688px;
  border-bottom-right-radius: 21.362228393554688px;
  font-size: 25px;
  font-weight: bold;
  color: white;
  border: 0;
  outline: 0;
}
</style>
