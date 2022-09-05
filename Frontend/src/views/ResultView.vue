<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1">나에게 꼭 맞는 학교는 ... </span>
    </div>
    <div
      class="star_box tooltip"
      v-if="(!isLoading || this.recommended === true) && !nodata"
    >
      🌟🌟🌟<span class="tooltiptext tooltip-right"
        >t-SNE 알고리즘이 추천한 대학입니다!</span
      >
    </div>
    <div class="boxwrapper">
      <div
        class="show"
        v-if="isLoading && this.recommended !== true && !nodata"
      >
        <img src="../assets/flying-airplane.gif" />
      </div>
      <div
        class="contents"
        v-if="(!isLoading || this.recommended === true) && !nodata"
      >
        <div class="box">
          <img :src="`${firstuniv.univ_image}`" class="box_image" />
          <div class="box_title">
            <span class="title_style">{{ firstuniv.name }}</span>
          </div>
          <div class="box_detail">
            <button class="box_link" @click="detail1">상세 정보 보기</button>
          </div>
        </div>

        <div class="box">
          <img :src="`${seconduniv.univ_image}`" class="box_image" />
          <div class="box_title">
            <span class="title_style">{{ seconduniv.name }}</span>
          </div>
          <div class="box_detail">
            <button class="box_link" @click="detail2">상세 정보 보기</button>
          </div>
        </div>
        <div class="box">
          <img :src="`${tsneuniv.univ_image}`" class="box_image" />
          <div class="box_title">
            <span class="title_style">{{ tsneuniv.name }}</span>
          </div>
          <div class="box_detail">
            <button class="box_link" @click="detail3">상세 정보 보기</button>
          </div>
        </div>
      </div>
      <div v-if="this.nodata === true">
        <span
          >올바르지 않은 검색입니다.<br />선택한 국가와 언어를 다시 한번
          확인해주세요<br />선택한 국가:{{ this.country }}<br />선택한 언어:{{
            JSON.parse(this.language)[0]
          }},{{ JSON.parse(this.language)[1] }}
        </span>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import axios from 'axios'
export default {
  components: {},
  data() {
    return {
      univlist: [],
      firstuniv: {},
      seconduniv: {},
      country: '',
      criteria: [],
      weather: '',
      language: [],
      semester: '',
      college: '',
      found: false,
      senddata: {
        country: this.country,
        semester: this.semester,
        college: this.college,
        criteria: this.criteria,
        wlevel: this.wlevel,
        language: this.language
      },
      isLoading: true,
      recommended: false,
      tsneuniv: {},
      nodata: false
    }
  },
  setup() {},
  create() {},
  mounted() {
    this.country = sessionStorage.getItem('country')
    this.criteria = sessionStorage.getItem('criteria')
    this.weather = sessionStorage.getItem('weather')
    this.language = sessionStorage.getItem('language')
    this.semester = sessionStorage.getItem('semester')
    this.college = sessionStorage.getItem('college')
    if (sessionStorage.getItem('recommended') === 'true') {
      this.recommended = true
    }
    this.getData()
  },
  unmounted() {},
  methods: {
    async getData() {
      try {
        const res = await axios.get('/api/recommend/', {
          params: {
            country: this.country,
            criteria: this.criteria,
            college: this.college,
            weather: this.weather,
            language: this.language,
            semester: this.semester
          }
        })
        this.univlist = res.data
        this.firstuniv = res.data[0]
        this.seconduniv = res.data[1]
        if (res.data[0].name === 'Nodata') {
          this.nodata = true
        } else {
          this.getData_2(res.data[0].name)
        }
        sessionStorage.setItem('recommended', 'true')
        setTimeout(this.recommend, 3000)
        setTimeout(this.loading, 3000)
      } catch (err) {
        console.error(err)
      }
    },
    async getData_2(tsnename) {
      try {
        const res = await axios.get('/api/tsneRecommend/', {
          params: {
            name: tsnename
          }
        })
        this.tsneuniv = res.data[0]
        if (this.seconduniv.name === res.data[0].name) {
          this.seconduniv = this.univlist[2]
          console.log('동일대학감지')
        }
      } catch (err) {
        console.error(err)
      }
    },
    detail1() {
      this.$router.push({
        name: 'detailresult',
        query: { name: this.firstuniv.name }
      })
    },
    detail2() {
      this.$router.push({
        name: 'detailresult',
        query: { name: this.seconduniv.name }
      })
    },
    detail3() {
      this.$router.push({
        name: 'detailresult',
        query: { name: this.tsneuniv.name }
      })
    },
    loading() {
      this.isLoading = false
    },
    recommend() {
      this.recommended = true
    }
  }
}
</script>
<style scoped>
.show {
  background-color: rgba(255, 255, 255, 1);
  margin-top: 5%;
  margin-left: 40%;
}
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 700px;
  display: flex;
  flex-direction: column;
}
.contents {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
  margin-left: 1%;
}
.box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: -10px 20px 40px rgba(0, 0, 0, 0.20000000298023224);
  background-color: rgba(255, 252.87500202655792, 252.87500202655792, 1);
  width: 358px;
  height: 425.6739196777344px;
  border-top-left-radius: 180px;
  border-top-right-radius: 180px;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  margin-left: 5%;
}
.star_box {
  margin-top: 6%;
  width: 120px;
  height: 30px;
  margin-left: 1038px;
  margin-bottom: 10px;
  font-size: 25px;
}

.boxwrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-left: 10%;
  margin-right: 10%;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  margin-left: 10%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 760px;
  height: 58px;
  font-family: Inter;
  text-align: left;
  font-size: 44.86062240600586px;
  letter-spacing: 0;
}
.box_image {
  width: 188px;
  height: 189px;
  border-top-left-radius: 82.5px;
  border-top-right-radius: 82.5px;
  border-bottom-left-radius: 82.5px;
  border-bottom-right-radius: 82.5px;
  background-repeat: no-repeat;
  background-size: cover;
  margin-bottom: 10%;
}
.box_title {
  width: 300px;
  height: 86.67391204833984px;
  text-align: center;
}
.title_style {
  color: rgba(0, 0, 0, 1);
  width: 326px;
  height: 32px;
  text-align: center;
  font-size: 24px;
  letter-spacing: 0;
  line-height: px;
}
.box_link {
  box-shadow: 0px 4px 4px
    rgba(
      40.999997556209564,
      183.00001949071884,
      228.0000016093254,
      0.15000000596046448
    );
  color: white;
  background-color: black;
  width: 243px;
  height: 40px;
  border-top-left-radius: 25px;
  border-top-right-radius: 25px;
  border-bottom-left-radius: 25px;
  border-bottom-right-radius: 25px;
  border: 0;
  outline: 0;
}
.tooltip {
  position: relative;
  display: block;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 190px;
  background-color: white;
  color: black;
  text-align: center;
  border-radius: 6px;
  padding: 10px;
  border: 1px solid black;

  position: absolute; /* 절대 위치를 사용 */
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  visibility: visible; /* hover 이벤트 발생시 영역을 보여줌 */
}

.tooltip .tooltip-right {
  top: -5px;
  left: 105%;
}

.tooltip .tooltip-right::after {
  top: 50%;
  right: 100%;
  margin-top: -5px;
  border-color: transparent black transparent transparent;
}
.tooltip .tooltiptext::after {
  content: ' ';
  position: absolute;
  border-style: solid;
  border-width: 5px;
}
a {
  text-decoration-line: none;
}
</style>
