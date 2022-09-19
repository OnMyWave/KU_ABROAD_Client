<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1">선호하는 날씨를 알려주세요!</span>
    </div>
    <div class="boxwrapper 1">
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="A1"
        >
          <button
            class="hothumid"
            value="A1"
            :disabled="!clicks[0] && clicked"
            @click="click"
          ></button>
        </div>
        <div class="box_msg">
          <button
            class="msg"
            value="A1"
            :disabled="!clicks[0] && clicked"
            @click="click"
          >
            {{ mouseovermsg[0] }}
          </button>
        </div>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="B1"
        >
          <button
            class="warmhumid"
            value="B1"
            :disabled="!clicks[1] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="B1"
          :disabled="!clicks[1] && clicked"
          @click="click"
        >
          {{ mouseovermsg[1] }}
        </button>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="C1"
        >
          <button
            class="coolhumid"
            value="C1"
            :disabled="!clicks[2] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="C1"
          :disabled="!clicks[2] && clicked"
          @click="click"
        >
          {{ mouseovermsg[2] }}
        </button>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="D1"
        >
          <button
            class="coldhumid"
            value="D1"
            :disabled="!clicks[3] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="D1"
          :disabled="!clicks[3] && clicked"
          @click="click"
        >
          {{ mouseovermsg[3] }}
        </button>
      </div>
    </div>
    <div class="boxwrapper 2">
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="A2"
        >
          <button
            class="hotdry"
            value="A2"
            :disabled="!clicks[4] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="A2"
          :disabled="!clicks[4] && clicked"
          @click="click"
        >
          {{ mouseovermsg[4] }}
        </button>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="B2"
        >
          <button
            class="warmdry"
            value="B2"
            :disabled="!clicks[5] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="B2"
          :disabled="!clicks[5] && clicked"
          @click="click"
        >
          {{ mouseovermsg[5] }}
        </button>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="C2"
        >
          <button
            class="cooldry"
            value="C2"
            :disabled="!clicks[6] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="C2"
          :disabled="!clicks[6] && clicked"
          @click="click"
        >
          {{ mouseovermsg[6] }}
        </button>
      </div>
      <div class="box">
        <div
          class="box_image"
          v-on:mouseover="mouseover"
          v-on:mouseleave="mouseleave"
          value="D2"
        >
          <button
            class="colddry"
            value="D2"
            :disabled="!clicks[7] && clicked"
            @click="click"
          ></button>
        </div>
        <button
          class="msg"
          value="D2"
          :disabled="!clicks[7] && clicked"
          @click="click"
        >
          {{ mouseovermsg[7] }}
        </button>
      </div>
    </div>
    <button @click="next" :class="{ blackbox: clicked, graybox: !clicked }">
      선택 완료
    </button>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      case: [],
      wlevel: '',
      clicks: [false, false, false, false, false, false, false, false],
      clicked: false,
      mouseover: false,
      mouseleave: true,
      pmouse: ''
    }
  },
  setup() {},
  create() {},
  mounted() {
    this.case = JSON.parse(sessionStorage.getItem('case'))
  },
  unmounted() {},
  watch: {},
  computed: {
    mouseovermsg() {
      if (this.mouseover == true) {
        if (this.pmouse == 'A1') {
          return [
            '온도:24.5℃ 강수량:205mm',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'A2') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '온도:28℃ 강수량:27mm',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'B1') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '온도:18℃ 강수량:170mm',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'B2') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '온도:12℃ 강수량:10mm',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'C1') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '온도:7.5℃ 강수량:70mm',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'C2') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '온도:7℃ 강수량:35mm',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'D1') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '온도:0℃ 강수량:95mm',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '❄️북유럽 같은 날씨🌲'
          ]
        } else if (this.pmouse == 'D2') {
          return [
            '☀️싱가포르 같은 날씨💦',
            '🌤서울 같은 날씨💧',
            '💨런던 같은 날씨🌧',
            '❄️퀘벡 같은 날씨💦',
            '☀️애리조나 같은 날씨🌵',
            '🌤캘리포니아 같은 날씨🍃',
            '💨동유럽 같은 날씨🍂',
            '온도:1℃ 강수량:45mm'
          ]
        }
      } else if (this.mouseover == false) {
        return [
          '☀️싱가포르 같은 날씨💦',
          '🌤서울 같은 날씨💧',
          '💨런던 같은 날씨🌧',
          '❄️퀘벡 같은 날씨💦',
          '☀️애리조나 같은 날씨🌵',
          '🌤캘리포니아 같은 날씨🍃',
          '💨동유럽 같은 날씨🍂',
          '❄️북유럽 같은 날씨🌲'
        ]
      }
    }
  },
  methods: {
    next() {
      if (this.wlevel !== '' && this.clicked === true) {
        sessionStorage.setItem('weather', this.wlevel)
        this.$router.push('language')
        sessionStorage.setItem('recommended', 'false')
      }
    },
    click(event) {
      if (event.target.value === 'A1') {
        this.clicks[0] = !this.clicks[0]
        this.clicked = !this.clicked
      } else if (event.target.value === 'B1') {
        this.clicks[1] = !this.clicks[1]
        this.clicked = !this.clicked
      } else if (event.target.value === 'C1') {
        this.clicks[2] = !this.clicks[2]
        this.clicked = !this.clicked
      } else if (event.target.value === 'D1') {
        this.clicks[3] = !this.clicks[3]
        this.clicked = !this.clicked
      } else if (event.target.value === 'A2') {
        this.clicks[4] = !this.clicks[4]
        this.clicked = !this.clicked
      } else if (event.target.value === 'B2') {
        this.clicks[5] = !this.clicks[5]
        this.clicked = !this.clicked
      } else if (event.target.value === 'C2') {
        this.clicks[6] = !this.clicks[6]
        this.clicked = !this.clicked
      } else if (event.target.value === 'D2') {
        this.clicks[7] = !this.clicks[7]
        this.clicked = !this.clicked
      }
      this.wlevel = event.target.value
    },
    mouseover(event) {
      this.pmouse = event.target.value
      this.mouseover = true
    },
    mouseleave() {
      this.pmouse = ''
      this.mouseover = false
    }
  }
}
</script>
<style scoped>
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 700px;
  display: flex;
  flex-direction: column;
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
  align-items: center;
  justify-content: center;
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 3%;
}
.box {
  margin-left: 1%;
  margin-bottom: 2%;
}
.hothumid {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/A1.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.hotdry {
  border-radius: 15px 15px 15px 15px;
  border-radius: 30px 30px 30px 30px;
  background-image: url('../assets/A2.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.warmhumid {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/B1.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.warmdry {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/B2.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.coolhumid {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/C1.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.cooldry {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/C2.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.coldhumid {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/D1.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.colddry {
  border-radius: 15px 15px 15px 15px;
  background-image: url('../assets/D2.png');
  background-repeat: no-repeat;
  background-size: cover;
  width: 303px;
  height: 184px;
  border: 2px solid black;
  outline: 0;
}
.msg {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 303px;
  height: 74px;
  line-height: 74px;
  font-size: 23px;
  font-weight: bold;
  border: 3px solid black;
  outline: 0;
}
a {
  text-decoration-line: none;
}
.btn_image {
  width: 294px;
  height: 185px;
}
.ifclick {
  background-color: gray;
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
  top: 980px;
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
  top: 980px;
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
