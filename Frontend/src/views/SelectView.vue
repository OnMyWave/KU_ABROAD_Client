<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1"
        >교환 생활에서 가장 중요한 기준은 무엇인가요?</span
      >
      <span class="intro_msg2">6가지를 중요한 순서대로 선택해주세요.</span>
    </div>
    <div class="selected 1">
      <h1 class="selected_criteria first">{{ importance[criteria[0]] }}</h1>
      <h1 class="arrow" v-if="this.criteria.length > 0">-></h1>
      <h1 class="selected_criteria second">{{ importance[criteria[1]] }}</h1>
      <h1 class="arrow" v-if="this.criteria.length > 1">-></h1>
      <h1 class="selected_criteria third">{{ importance[criteria[2]] }}</h1>
      <h1 class="arrow" v-if="this.criteria.length > 2">-></h1>
    </div>
    <div class="selected 2">
      <h1 class="selected_criteria fourth">{{ importance[criteria[3]] }}</h1>
      <h1 class="arrow" v-if="this.criteria.length > 3">-></h1>
      <h1 class="selected_criteria fifth">{{ importance[criteria[4]] }}</h1>
      <h1 class="arrow" v-if="this.criteria.length > 4">-></h1>
      <h1 class="selected_criteria sixth">{{ importance[criteria[5]] }}</h1>
    </div>
    <div class="boxwrapper">
      <button
        :class="{ weather: !clicked[0], weather_1: clicked[0] }"
        @click="Weather"
      >
        날씨 🌤
      </button>
      <button
        :class="{ dormitory: !clicked[1], dormitory_1: clicked[1] }"
        @click="Dormitory"
      >
        1인실 기숙사 🛏
      </button>
      <button
        :class="{ money: !clicked[4], money_1: clicked[4] }"
        @click="Money"
      >
        저렴한 생활비 💸
      </button>
      <button
        :class="{ transportation: !clicked[3], transportation_1: clicked[3] }"
        @click="Transportation"
      >
        편리한 교통 🚗
      </button>

      <button
        :class="{ ranking: !clicked[5], ranking_1: clicked[5] }"
        @click="Ranking"
      >
        높은 학교 랭킹 📌
      </button>
      <button
        :class="{ language: !clicked[2], language_1: clicked[2] }"
        @click="Language"
      >
        언어 🔤
      </button>
    </div>
    <button
      :class="{ graynext: criteria.length < 6, next: criteria.length === 6 }"
      @click="next"
      :disabled="criteria.length != 6"
    >
      Next
    </button>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      criteria: [],
      clicked: [false, false, false, false, false, false],
      importance: {
        weather: '날씨 🌤',
        dormitory: '1인실 기숙사 🛏',
        language: '언어 🔤',
        transportation: '편리한 교통 🚗',
        money: '저렴한 생활비 💸',
        ranking: '높은 학교 랭킹 📌'
      }
    }
  },
  unmounted() {},
  methods: {
    Weather() {
      if (this.clicked[0] === false) {
        this.criteria.push('weather')
        this.clicked[0] = true
      } else if (this.clicked[0] === true) {
        this.criteria = this.criteria.filter((element) => element !== 'weather')
        this.clicked[0] = false
      }
    },
    Dormitory() {
      if (this.clicked[1] === false) {
        this.criteria.push('dormitory')
        this.clicked[1] = true
      } else if (this.clicked[1] === true) {
        this.criteria = this.criteria.filter(
          (element) => element !== 'dormitory'
        )
        this.clicked[1] = false
      }
    },
    Language() {
      if (this.clicked[2] === false) {
        this.criteria.push('language')
        this.clicked[2] = true
      } else if (this.clicked[2] === true) {
        this.criteria = this.criteria.filter(
          (element) => element !== 'language'
        )
        this.clicked[2] = false
      }
    },
    Transportation() {
      if (this.clicked[3] === false) {
        this.criteria.push('transportation')
        this.clicked[3] = true
      } else if (this.clicked[3] === true) {
        this.criteria = this.criteria.filter(
          (element) => element !== 'transportation'
        )
        this.clicked[3] = false
      }
    },
    Money() {
      if (this.clicked[4] === false) {
        this.criteria.push('money')
        this.clicked[4] = true
      } else if (this.clicked[4] === true) {
        this.criteria = this.criteria.filter((element) => element !== 'money')
        this.clicked[4] = false
      }
    },
    Ranking() {
      if (this.clicked[5] === false) {
        this.criteria.push('ranking')
        this.clicked[5] = true
      } else if (this.clicked[5] === true) {
        this.criteria = this.criteria.filter((element) => element !== 'ranking')
        this.clicked[5] = false
      }
    },
    next() {
      sessionStorage.setItem('criteria', JSON.stringify(this.criteria))
      this.$router.push('weather')
      sessionStorage.setItem('recommended', 'false')
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
.selected {
  margin-top: 30px;
}
.selected_criteria {
  float: left;
  margin-left: 2.5%;
}
.selected_criteria.first {
  margin-left: 15%;
}
.selected_criteria.fourth {
  margin-left: 30%;
}
.arrow {
  margin-left: 2.5%;
  float: left;
}
.boxwrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  margin-left: 10%;
  margin-right: 5%;
  margin-top: 3.5%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 1200px;
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

.weather {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 263.0137023925781px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  font-weight: 550;
  margin-left: 2%;
  margin-top: 2%;
  border: 0;
  outline: 0;
}
.weather_1 {
  background-color: gray;
  width: 263.0137023925781px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  font-weight: 550;
  margin-left: 2%;
  margin-top: 2%;
  border: 0;
  outline: 0;
}
.weather:active {
  background-color: gray;
}
.dormitory:active {
  background-color: gray;
}

.dormitory {
  margin-left: 2%;
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 404.7488708496094px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  margin-top: 2%;
  border: 0;
  outline: 0;
}
.dormitory_1 {
  margin-left: 2%;
  margin-top: 2%;
  background-color: gray;
  width: 404.7488708496094px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}

.language {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  margin-left: 2%;
  margin-top: 2%;
  width: 263.0137023925781px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.language_1 {
  margin-left: 2%;
  margin-top: 2%;
  background-color: gray;
  width: 263.0137023925781px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.language:active {
  background-color: gray;
}
.transportation {
  margin-left: 2%;
  margin-top: 2%;
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 387.214599609375px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.transportation_1 {
  margin-left: 2%;
  margin-top: 2%;
  background-color: gray;
  width: 387.214599609375px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.transportation:active {
  background-color: gray;
}
.money {
  margin-left: 2%;
  margin-top: 2%;
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 395.9817199707031px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.money_1 {
  margin-top: 2%;
  margin-left: 2%;
  background-color: gray;
  width: 395.9817199707031px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.money:active {
  background-color: gray;
}
.ranking {
  margin-left: 2%;
  margin-top: 2%;
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 414.9771728515625px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.ranking_1 {
  margin-left: 2%;
  margin-top: 2%;
  background-color: gray;
  width: 414.9771728515625px;
  height: 137.35159301757812px;
  border-top-left-radius: 31.214214324951172px;
  border-top-right-radius: 31.214214324951172px;
  border-bottom-left-radius: 31.214214324951172px;
  border-bottom-right-radius: 31.214214324951172px;
  cursor: pointer;
  text-align: center;
  font-size: 35px;
  color: white;
  line-height: 137.35159301757812px;
  font-weight: 550;
  border: 0;
  outline: 0;
}
.next {
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
.graynext {
  background-color: gray;
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
.ranking:active {
  background-color: gray;
}
a {
  text-decoration-line: none;
}
</style>
