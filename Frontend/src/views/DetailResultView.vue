<template>
  <div class="container">
    <div class="univ_info">
      <img class="univ_image" :src="`${data.univ_image}`" />
      <div class="univ_title">
        <span class="univ_name">{{ data.name }}</span>
        <span class="box_msg city">{{ data.city }}, {{ data.country }}</span>
        <span class="box_msg language">
          사용언어 :
          <span class="red">{{ data.language }}</span>
        </span>
      </div>
    </div>
    <div class="empty_box f">
      <div class="box">
        <div class="flexbox">
          <div class="box_title_weather">날씨</div>
          <select class="select_semester" v-model="semester">
            <option value="1">1학기&nbsp;({{ data.sem1_period }})</option>
            <option value="2">2학기&nbsp;({{ data.sem2_period }})</option>
          </select>
        </div>
        <div class="center">
          <span class="box_msg" v-if="semester === '1'"
            >🌡평균 기온
            <span class="red">{{ data.sem1_temp_mean.toFixed(2) }} </span
            >℃</span
          >
          <span class="box_msg" v-if="semester === '2'"
            >🌡평균 기온
            <span class="red">{{ data.sem2_temp_mean.toFixed(2) }} </span
            >℃</span
          >
          <span class="box_msg" v-if="semester === '1'"
            >💦월평균 강수량
            <span class="blue">{{ data.sem1_rain_mean.toFixed(2) }} </span
            >mm</span
          >
          <span class="box_msg" v-if="semester === '2'"
            >💦월평균 강수량
            <span class="blue">{{ data.sem2_rain_mean.toFixed(2) }} </span
            >mm</span
          >
        </div>
      </div>
      <div class="box">
        <span class="box_title">안전도</span>
        <div class="center">
          <span class="box_msg">{{ crime[this.data.crime_idx - 1] }}</span>
        </div>
      </div>
      <div class="box">
        <div class="flexbox">
          <span class="box_title_qs">&nbsp;&nbsp;&nbsp;&nbsp;QS Ranking</span>
          <select v-model="colleges" class="select_semester">
            <option class="coloption" value="h">인문대학</option>
            <option class="coloption" value="m">사회과학/정경대학</option>
            <option class="coloption" value="t">공과대학</option>
            <option class="coloption" value="n">자연대학</option>
            <option class="coloption" value="l">생명과학대학</option>
          </select>
        </div>
        <div class="center">
          <span class="college">{{ category[rank[colleges]] }}</span>
          <span class="rank_msg"
            ><span class="red" v-if="data[rank[colleges]] !== '999'"
              >{{ data[rank[colleges]] }}위</span
            ><span class="red x" v-if="data[rank[colleges]] === '999'"
              >해당계열은 존재하지 않아요.</span
            ></span
          >
        </div>
      </div>
    </div>
    <div class="big_box">
      <span class="box_title">대학 지도</span>
      <iframe
        class="googlemap"
        :src="`https://www.google.com/maps/embed/v1/place?key=AIzaSyB1DPd6H8s2qZCP90-USY4ZCCLdnAqve4g&q=${data.name}&region=KR&language=ko`"
      />
    </div>
    <div class="big_box travel">
      <div class="flexbox">
        <span class="box_title">주변 여행지</span>
        <a class="link" :href="data.trip_link">사이트 방문하기 </a>
      </div>
      <div class="image_container">
        <div class="image_box">
          <img
            :src="`${data.image1}`"
            class="image_src"
            width="250px"
            height="222px"
          />
          <div class="image_msg">{{ data.title1 }}</div>
        </div>
        <div class="image_box">
          <img
            :src="`${data.image2}`"
            class="image_src"
            width="250px"
            height="222px"
          />
          <div class="image_msg">{{ data.title2 }}</div>
        </div>
        <div class="image_box">
          <img
            :src="`${data.image3}`"
            class="image_src"
            width="250px"
            height="222px"
          />
          <div class="image_msg">{{ data.title3 }}</div>
        </div>
      </div>
    </div>
    <div class="big_box">
      <span class="box_title score">자격 요건</span>
      <div class="half_box f">
        <div class="small_box test">
          <span class="small_box_msg test">[어학]</span>
          <div class="box_item_test">
            <div class="small_box_msg_t">TOFEL :</div>
            <div class="small_box_msg_t">IELTS :</div>
            <div class="small_box_msg_tt">ETC :</div>
          </div>
          <div class="score_box">
            <div class="score f">{{ data.TOEFL }}</div>
            <div class="score f">{{ data.IELTS }}</div>
            <div class="score s">{{ data.etc }}</div>
          </div>
        </div>
        <div class="small_box">
          <span class="small_box_msg gpa">[학점]</span>
          <div class="box_item">
            <span class="small_box_msg"
              ><span class="red"> {{ data.gpa }}</span> 이상</span
            >
          </div>
        </div>
      </div>
      <div class="half_box s">
        <div class="small_box">
          <span class="small_box_msg">[1년 파견]</span>
          <div class="box_item">
            <span class="small_box_msg k"
              >1년 파견 {{ poss[data.one_year] }}</span
            >
          </div>
        </div>
        <div class="small_box">
          <span class="small_box_msg">[특이사항]</span>
          <div class="small_box block">
            <div class="small_box_msg uniq" v-if="data.uniq === '.'">
              해당사항 없음
            </div>
            <div class="small_box_msg uniq" v-if="data.uniq !== '.'">
              {{ uniq[data.uniq[0]] }}
            </div>
            <div class="small_box_msg uniq" v-if="data.uniq !== '.'">
              {{ uniq[data.uniq[3]] }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="empty_box s">
      <div class="box">
        <span class="box_title">물가</span>
        <div class="center">
          <span class="box_msg">{{ living[data.living_idx - 1] }}</span>
        </div>
      </div>
      <div class="box">
        <span class="box_title">기숙사</span>
        <div class="center">
          <span class="box_msg" v-show="data.domi === 1">{{ dorm[0] }}</span>
          <span class="box_msg" v-show="data.domi === 0">{{ dorm[1] }}</span>
          <span class="box_msg" v-show="data.domi === 2">{{ dorm[2] }}</span>
        </div>
      </div>
      <div class="box">
        <span class="box_title">교통</span>
        <div class="center">
          <span class="box_msg">버스🚌 {{ exi[data.bus] }}</span>
          <span class="box_msg">지하철🚆 {{ exi[data.train] }}</span>
        </div>
      </div>
    </div>
    <div class="big_box_talk">
      <span class="box_title">선배들의 한 마디</span>
      <span class="long_msg"
        >*본 정보는 본교 교환학생 수기를 기반으로 선정한 주요 정보입니다.</span
      >
      <div class="talkbox">
        <div class="small_talkbox">
          <div class="small_box_msg talk">
            <span class="talk_bubble">{{ data.hashtag1 }}</span>
          </div>
          <div class="small_box_msg place">
            <span class="talk_bubble_2" v-if="data.recommend_place1 !== '.'"
              ><span class="placehashtag">{{ data.recommend_place1 }}</span
              >에 방문해 보세요!
            </span>
          </div>
        </div>
        <div class="small_talkbox">
          <div class="small_box_msg talk">
            <span class="talk_bubble">{{ data.hashtag2 }}</span>
          </div>
          <div class="small_box_msg place">
            <span class="talk_bubble_2" v-if="data.recommend_place2 !== '.'"
              ><span class="placehashtag">{{ data.recommend_place2 }}</span
              >에 여행을 가보세요!
            </span>
          </div>
        </div>
        <div class="small_box_msg talk">
          <span class="talk_bubble">{{ data.hashtag3 }}</span>
        </div>
      </div>
      <div class="balloon"></div>
    </div>
    <div class="big_box">
      <span class="box_title">사회적 가치🍀</span>
      <div class="half_box">
        <div class="quater_box">
          <span class="quater_box_title">[Global Vegan Index]</span>
          <span class="quater_box_msg"
            >Global Vegan Index는 상대적인 비건 지수를 의미합니다.
            <br />초록색에 가까울수록 비건 친화적인 국가/도시를 의미합니다.<br />
            Index는 비건 레스토랑 수와 해당 국가의 동물 친화도 등을
            포함합니다.</span
          >
        </div>
        <div class="quater_box">
          <div class="barwrapper">
            <span class="bar_num">50</span>
            <div class="bar">
              <div
                class="circle"
                :style="{ marginLeft: gvi_idx + 'px' }"
                v-show="data.gvi_idx !== 1"
              ></div>
            </div>
            <span class="bar_num">100</span>
          </div>
        </div>
      </div>
      <div class="half_box">
        <div class="quater_box">
          <span class="quater_box_title"
            >[Sustainable Development Goals Score]</span
          >
          <span class="quater_box_msg"
            >Sustainable Development Goals Score는 지속 가능한 발전 지수를
            의미합니다. Index는 well-being 수치, 성평등, 위생, 사회 기반 시설,
            기후 행동, 평화 정도 등을 포함합니다.</span
          >
        </div>
        <div class="quater_box">
          <div class="barwrapper">
            <span class="bar_num">50</span>
            <div class="bar">
              <div
                class="circle"
                :style="{ marginLeft: sdg_idx + 'px' }"
                v-show="data.sdg_idx !== 1"
              ></div>
            </div>
            <span class="bar_num">100</span>
          </div>
        </div>
      </div>
    </div>
    <div class="wordcloud_box">
      <div class="flexbox">
        <div class="box_title wordcloud">WordCloud</div>
        <div class="wordcloud_dropdown">
          <select class="wordcloud_select" v-model="wordcloud">
            <option
              :value="wordcloud.value"
              :key="i"
              v-for="(wordcloud, i) in wordcloud_options"
            >
              {{ wordcloud.text }}
            </option>
          </select>
        </div>
      </div>
      <img class="wordcloud_img" :src="`${data[wordcloud]}`" />
    </div>
    <div class="empty_box t">
      <br /><br /><br /><br /><br /><br /><br /><br />
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  components: {},
  data() {
    return {
      data: {},
      crime: ['안전해요🎶', '보통이에요💬', '약간 위험해요💦', '위험해요🚨'],
      living: ['저렴해요😁', '보통이에요🙂', '비싸요😣', '매우 비싸요😭'],
      rank: { h: 'r1', t: 'r2', l: 'r3', n: 'r4', m: 'r5' },
      category: {
        r1: '인문계열',
        r2: '공과계열',
        r3: '생명과학계열',
        r4: '자연과학계열',
        r5: '사회과학/경영계열'
      },
      dorm: ['기숙사가 있어요😀', '기숙사가 없어요🥲', '1인실이 있어요!😃'],
      exi: ['없어요!', '있어요!'],
      poss: ['불가능해요!', '가능해요!'],
      uniq: {
        A: '영역별 세부 점수 요건 있음',
        B: '전공별 요구 점수 다름',
        C: '기타 언어 강의 수강시 해당언어 점수 요구',
        D: '특정 과목 수강 시 더 높은 점수/추가 TEST 요구'
      },
      u: [],
      univ_name: '',
      univlist: [],
      semester: '1',
      colleges: '',
      wordcloud_options: [
        { value: 'wordcloud1_url', text: '지원절차' },
        { value: 'wordcloud2_url', text: '비자 준비과정' },
        { value: 'wordcloud3_url', text: '날씨 및 환경' },
        { value: 'wordcloud4_url', text: '수업' },
        { value: 'wordcloud5_url', text: '숙소 및 식사' },
        { value: 'wordcloud6_url', text: '학교 기타 정보' },
        { value: 'wordcloud7_url', text: 'International Office' },
        { value: 'wordcloud8_url', text: '기타 사항' },
        { value: 'wordcloud9_url', text: '전반적 의견' }
      ],
      wordcloud: 'wordcloud1_url'
    }
  },
  setup() {},
  create() {},
  mounted() {
    this.univ_name = this.$route.query.name
    this.getData()
    if (sessionStorage.getItem('college')) {
      this.colleges = sessionStorage.getItem('college')
    } else {
      this.colleges = 'm'
    }
    if (sessionStorage.getItem('semester')) {
      this.semester = sessionStorage.getItem('semester')
    } else {
      this.semester = '1'
    }
  },
  computed: {},
  unmounted() {},
  methods: {
    async getData() {
      try {
        const res = await axios.get('/api/univ/', {
          params: { name: this.univ_name }
        })
        this.univlist = res.data
        this.data = this.univlist[0]
      } catch (err) {
        console.error(err)
      }
    },
    loading() {
      this.isLoading = false
    }
  },
  computed: {
    gvi_idx() {
      return Math.max((24 * (this.data.gvi_idx - 50)) / 5, 0)
    },
    sdg_idx() {
      return Math.max((24 * (this.data.sdg_idx - 50)) / 5, 0)
    }
  }
}
</script>
<style scoped>
.bar_num {
  margin-left: 3%;
  margin-right: 3%;
}
.barwrapper {
  display: flex;
  flex-direction: row;
}
.circle {
  box-shadow: 0px 0px 1.0773364305496216px rgba(0, 0, 0, 0.3499999940395355);
  background-image: linear-gradient(
    0deg,
    rgba(235.87500303983688, 235.87500303983688, 235.87500303983688, 1) 0%,
    rgba(200.82910358905792, 200.82910358905792, 200.82910358905792, 1)
      92.70833134651184%
  );
  width: 18px;
  height: 18px;
  border-top-left-radius: 26.93341064453125px;
  border-top-right-radius: 26.93341064453125px;
  border-bottom-left-radius: 26.93341064453125px;
  border-bottom-right-radius: 26.93341064453125px;
  z-index: 2;
}
.quater_box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 3%;
}
.quater_box_title {
  width: 400px;
  height: 40px;
  margin-left: 1%;
}
.quater_box_msg {
  margin-left: 1%;
  font-size: 15px;
  width: 420px;
  height: 40px;
}
.bar {
  z-index: 1;
  background-image: linear-gradient(to right, red, green);
  width: 300px;
  height: 18px;
  border-top-left-radius: 26.93341064453125px;
  border-top-right-radius: 26.93341064453125px;
  border-bottom-left-radius: 26.93341064453125px;
  border-bottom-right-radius: 26.93341064453125px;
}
.small_box_msg {
  margin-left: 3%;
  margin-top: 1%;
  width: 180px;
  height: 40px;
  font-weight: normal;
}
.small_box_msg.uniq {
  width: 250px;
  font-size: 20px;
}
.small_box_msg.talk {
  width: 600px;
  margin-top: 2.3%;
}
.small_box_msg.gpa {
  width: 100px;
}
.small_box_msg.place {
  width: 300px;
  margin-top: 2.3%;
}
.small_box_msg.test {
  width: 120px;
  height: 100px;
}
.half_box {
  display: flex;
  flex-direction: row;
  margin-bottom: 3%;
  width: 900px;
  height: 100px;
}
.half_box.f {
  font-size: 20px;
  font-weight: bold;
}
.half_box.s {
  font-size: 20px;
  font-weight: bold;
}
.small_box {
  display: flex;
  flex-direction: row;
  width: 450px;
  height: 70px;
}
.small_box.test {
  height: 100px;
}
.small_box.block {
  display: block;
}
.box_item {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  margin-left: 5%;
}
.box_item_test {
  display: block;
  font-size: 20px;
  margin-left: 0;
  font-weight: normal;
}
.long_msg {
  color: rgba(102.00000151991844, 102.00000151991844, 102.00000151991844, 1);
  width: 500px;
  height: 20px;
  font-family: Inter;
  font-size: 15px;
  letter-spacing: 0;
  margin-left: 3%;
  margin-bottom: 2%;
}
.center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 15%;
}
.college {
  font-size: 20px;
}
.rank_msg {
  font-size: 30px;
}
.blue {
  color: blue;
}
.red {
  color: red;
}
.red.x {
  font-size: 15px;
}
.small_box_msg.k {
  width: 200px;
}
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 1300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 3%;
}
.univ_info {
  display: flex;
  width: 1080px;
  height: 300px;
  flex-direction: column;
  margin-bottom: 3%;
}
.univ_title {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 918px;
  height: 130px;
  position: absolute;
  left: 258px;
  top: 450px;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: left;
}
.univ_image {
  border-radius: 15px 15px 15px 15px;
  background-color: rgba(
    217.0000022649765,
    217.0000022649765,
    217.0000022649765,
    1
  );
  width: 1080px;
  height: 300px;
  left: 0px;
  top: 0px;
  position: relative;
  z-index: 1;
}
.box {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 281px;
  height: 222px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.empty_box {
  width: 918px;
  height: 300px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 3%;
}
.empty_box.f {
  margin-top: 65px;
}
.empty_box.t {
  height: 150px;
}
.big_box {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 918px;
  height: 350px;
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  flex-wrap: wrap;
}
.big_box_talk {
  height: 500px;
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 918px;
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  flex-wrap: wrap;
}
.big_box.travel {
  height: 400px;
}
.univ_name {
  color: rgba(0, 0, 0, 1);
  width: 1000px;
  height: 51px;
  font-family: Inter;
  text-align: left;
  font-size: 26.297607421875px;
  letter-spacing: 0;
  margin-top: 2%;
  margin-left: 5%;
}
.googlemap {
  background-color: rgba(
    217.0000022649765,
    217.0000022649765,
    217.0000022649765,
    1
  );
  width: 886px;
  height: 248px;
  margin-left: 2%;
  margin-bottom: 2%;
}
.image_src {
  border-radius: 15px 15px 15px 15px;
  transform: rotate(-0.37949814332678566deg);
  width: 280.861328125px;
  height: 222.68487548828125px;
  background-repeat: no-repeat;
  background-size: cover;
}
.image_msg {
  border-radius: 15px 15px 15px 15px;
  background-color: rgba(255, 255, 255, 1);
  width: 275px;
  height: 40px;
  border-top-left-radius: 13.790614128112793px;
  border-top-right-radius: 13.790614128112793px;
  border-bottom-left-radius: 13.790614128112793px;
  border-bottom-right-radius: 13.790614128112793px;
  margin-left: 5%;
  text-align: center;
  font-weight: 20;
}
.image_container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
.box_title {
  color: (0, 0, 0, 1);
  width: 250px;
  height: 30px;
  font-family: Inter;
  text-align: left;
  font-size: 20px;
  letter-spacing: 0;
  margin-left: 3%;
  margin-top: 2%;
  margin-bottom: 2%;
  font-weight: bold;
}
.box_title_weather {
  margin-top: 10px;
  width: 70px;
  margin-left: 1px;
  font-size: 20px;
  font-weight: bold;
}
.box_title_qs {
  margin-top: 10px;
  width: 70px;
  margin-left: 1px;
  font-size: 20px;
  font-weight: bold;
}
.box_title.wordcloud {
  font-size: 26px;
}
.box_msg {
  color: black;
  width: 250px;
  height: 51px;
  font-family: Inter;
  font-size: 20px;
  letter-spacing: 0;
  margin-left: 5%;
  text-align: center;
}
.box_msg.city {
  margin-top: 8px;
  width: 450px;
  text-align: left;
}
.box_msg.language {
  width: 350px;
  text-align: left;
}
a {
  text-decoration-line: none;
}
.talkbox {
  width: 918px;
  height: 200px;
  display: block;
}
.talk_bubble {
  position: relative;
  background: pink;
  border-radius: 0.4em;
  padding: 10px;
  font-weight: bold;
}

.talk_bubble:after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 0;
  height: 0;
  border: 7px solid transparent;
  border-top-color: pink;
  border-bottom: 0;
  border-left: 0;
  margin-left: -3.5px;
  margin-bottom: -7px;
}
.talk_bubble_2 {
  position: relative;
  background: lightgreen;
  border-radius: 0.4em;
  padding: 10px;
  float: right;
  margin-right: 30px;
  font-weight: bold;
}
.talk_bubble_2:after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 10%;
  width: 0;
  height: 0;
  border: 7px solid transparent;
  border-top-color: lightgreen;
  border-bottom: 0;
  border-right: 0;
  margin-left: -3.5px;
  margin-bottom: -7px;
}
.select_semester {
  margin-left: 20px;
  padding: 5px;
  border-radius: 30px;
  margin-top: 8px;
}
.flexbox {
  display: flex;
}
.small_talkbox {
  width: 918px;
  height: 50px;
  display: flex;
}
.wordcloud_box {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 918px;
  height: 650px;
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  flex-wrap: wrap;
}
.wordcloud_dropdown {
  width: 300px;
  height: 66px;
  margin-left: 365px;
  margin-top: 2%;
}
.wordcloud_img {
  width: 910px;
  height: 500px;
  margin-left: 5px;
  margin-bottom: 10px;
}
.wordcloud_select {
  padding: 5px;
  text-align-last: center;
  text-align: center;
  width: 180px;
  height: 50px;
  border-radius: 50px;
  border: 1px solid black;
}
.link {
  color: black;
  margin-top: 1%;
  margin-left: 480px;
  border-radius: 40px;
  border: 1px solid black;
  height: 30px;
  line-height: 30px;
  padding: 8px;
}
.score_box {
  width: 210px;
  height: 100px;
}
.score {
  width: 210px;
}
.score.f {
  height: 25px;
  font-weight: normal;
}
.score.s {
  height: 50px;
  font-weight: normal;
}
.small_box_msg_t {
  width: 120px;
  height: 25px;

  font-size: 22px;
  text-align: left;
}
.small_box_msg_tt {
  width: 120px;
  height: 50px;

  font-size: 22px;
  text-align: left;
}
.box_title.score {
  font-size: 22px;
}
</style>
