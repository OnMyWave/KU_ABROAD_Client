<template>
  <div class="container" :style="{ height: heightchange + 650 + 'px' }">
    <div class="intro_box">
      <div class="intro_msg1">떠나고 싶은 학교를 찾아보세요 !</div>
      <div class="intro_msg2">학교 사진을 누르면 상세정보가 나와요.</div>
    </div>
    <div class="search_box">
      <input
        class="search"
        type="text"
        v-model="search_name"
        @keyup.enter="getData"
        placeholder="학교명을 영어로 입력하세요"
      />
      <button class="search_button" @click="getData"></button>
    </div>
    <div class="continent_box">
      <div class="continent_box_samll first">
        <button
          :class="{
            'continent_img_circle northamerica': !continent_clicked[0],
            'continent_img_circle northamerica clicked': continent_clicked[0]
          }"
          @click="continentclick_1"
          :disabled="continent_clicks && !continent_clicked[0]"
        ></button>
        <div class="continent_msg">북미</div>
      </div>
      <div class="continent_box_samll second">
        <button
          :class="{
            'continent_img_circle europe': !continent_clicked[1],
            'continent_img_circle europe clicked': continent_clicked[1]
          }"
          @click="continentclick_2"
          :disabled="continent_clicks && !continent_clicked[1]"
        ></button>
        <div class="continent_msg">유럽</div>
      </div>
      <div class="continent_box_samll third">
        <button
          :class="{
            'continent_img_circle asia': !continent_clicked[2],
            'continent_img_circle asia clicked': continent_clicked[2]
          }"
          @click="continentclick_3"
          :disabled="continent_clicks && !continent_clicked[2]"
        ></button>
        <div class="continent_msg">아시아</div>
      </div>
      <div class="continent_box_samll fourth">
        <button
          :class="{
            'continent_img_circle oceania': !continent_clicked[3],
            'continent_img_circle oceania clicked': continent_clicked[3]
          }"
          @click="continentclick_4"
          :disabled="continent_clicks && !continent_clicked[3]"
        ></button>
        <div class="continent_msg">오세아니아</div>
      </div>
      <div class="continent_box_samll fifth">
        <button
          :class="{
            'continent_img_circle southamerica': !continent_clicked[4],
            'continent_img_circle southamerica clicked': continent_clicked[4]
          }"
          @click="continentclick_5"
          :disabled="continent_clicks && !continent_clicked[4]"
        ></button>
        <div class="continent_msg">남미</div>
      </div>
    </div>
    <div class="detailsearch_box">
      <div class="detailsearch_dropdown_box first">
        <select class="detailsearch_dropdown weather" v-model="weather">
          <option
            :value="weather.value"
            :key="i"
            v-for="(weather, i) in weather_options"
          >
            {{ weather.text }}
          </option>
        </select>
      </div>
      <div class="detailsearch_dropdown_box second">
        <select class="detailsearch_dropdown language" v-model="language">
          <option
            :value="language.value"
            :key="i"
            v-for="(language, i) in language_options"
          >
            {{ language.text }}
          </option>
        </select>
      </div>
      <div class="detailsearch_dropdown_box third">
        <select class="detailsearch_dropdown dormitory" v-model="dormitory">
          <option
            :value="dormitory.value"
            :key="i"
            v-for="(dormitory, i) in dormitory_options"
          >
            {{ dormitory.text }}
          </option>
        </select>
      </div>
      <div class="detailsearch_dropdown_box fourth">
        <select class="detailsearch_dropdown order" v-model="order">
          <option
            :value="order.value"
            :key="i"
            v-for="(order, i) in order_options"
          >
            {{ order.text }}
          </option>
        </select>
      </div>
      <div class="detailsearch_dropdown_box fifth">
        <select
          class="detailsearch_dropdown college"
          v-model="college"
          v-show="order === 'qs'"
        >
          <option
            :value="college.value"
            :key="i"
            v-for="(college, i) in college_options"
          >
            {{ college.text }}
          </option>
        </select>
      </div>
      <div class="detailsearch_dropdown_box sixth">
        <button class="search_button_2" @click="Update"></button>
      </div>
    </div>
    <div
      class="univlist_box"
      :key="n"
      v-for="n in this.seperated_univ2[present_page - 1].length"
    >
      <div
        :key="i"
        v-for="(univ, i) in this.seperated_univ2[present_page - 1][n - 1]"
      >
        <div class="univ_box" v-if="univ.name !== 'Nodata'">
          <button
            class="univimg_box"
            :style="{ backgroundImage: 'url(' + univ.univ_image + ')' }"
            @click="detailresult"
            :value="univ.name"
          ></button>
          <div class="univ_name">
            {{ univ.name }}
          </div>
          <div class="univ_country">
            {{ univ.city }}&nbsp;,&nbsp;{{ univ.country }}
          </div>
        </div>
      </div>
    </div>
    <div class="page_number_box" v-if="number > 0">
      <div class="page_number_container">
        <button class="left_arrow" @click="page_down">&#60;</button>
        <div class="page_number">{{ present_page }}/{{ total_page }}</div>
        <button class="right_arrow" @click="page_up">&#62;</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      search_name: '',
      continent_name: '',
      continent_clicks: false,
      continent_clicked: [false, false, false, false, false],
      weather_options: [
        { value: '', text: '날씨 선택' },
        { value: 'A1', text: '싱가포르 같은 날씨' },
        { value: 'B1', text: '서울 같은 날씨' },
        { value: 'C1', text: '런던 같은 날씨' },
        { value: 'D1', text: '퀘벡 같은 날씨' },
        { value: 'A2', text: '애리조나 같은 날씨' },
        { value: 'B2', text: '캘리포니아 같은 날씨' },
        { value: 'C2', text: '동유럽 같은 날씨' },
        { value: 'D2', text: '북유럽 같은 날씨' }
      ],
      language_options: [
        { value: '', text: '언어 선택' },
        { value: 'English', text: '영어' },
        { value: 'German', text: '독일어' },
        { value: 'Spanish', text: '스페인어' },
        { value: 'Chinese', text: '중국어' },
        { value: 'Japanese', text: '일본어' },
        { value: 'French', text: '프랑스어' },
        { value: 'Russian', text: '러시아어' },
        { value: 'Italian', text: '이탈리아어' },
        { value: 'Polish', text: '폴란드어' }
      ],
      dormitory_options: [
        { value: '', text: '기숙사' },
        { value: 2, text: '1인실 있음' },
        { value: 1, text: '있음' },
        { value: 0, text: '없음' }
      ],
      order_options: [
        { value: '', text: '순서선택' },
        { value: 'qs', text: 'QS랭킹 높은순' },
        { value: 'trans', text: '교통 편리한순' },
        { value: 'money', text: '저렴한 생활비순' }
      ],
      college_options: [
        { value: 's1', text: '인문대학' },
        { value: 's5', text: '사회과학/정경대학' },
        { value: 's2', text: '공과대학' },
        { value: 's4', text: '자연대학' },
        { value: 's3', text: '생명과학대학' }
      ],
      weather: '',
      language: '',
      dormitory: '',
      order: '',
      detailsearch_clicked: [false, false, false],
      selected_univ: [],
      number: 0,
      seperated_univ: [],
      seperated_univ2: [[], [], [], [], [], [], [], []],
      page: [false, false, false, false],
      present_page: 1,
      data: {},
      college: 's1',
      isLoading: true
    }
  },
  setup() {},
  create() {},
  mounted() {
    if (sessionStorage.getItem('search_continent')) {
      this.continent_name = sessionStorage.getItem('search_continent')
    }
    if (sessionStorage.getItem('search_weather')) {
      this.weather = sessionStorage.getItem('search_weather')
    }
    if (sessionStorage.getItem('search_language')) {
      this.language = sessionStorage.getItem('search_language')
    }
    if (sessionStorage.getItem('search_dormitory')) {
      this.dormitory = sessionStorage.getItem('search_dormitory')
    }
    if (sessionStorage.getItem('search_order')) {
      this.order = sessionStorage.getItem('search_order')
    }
    if (sessionStorage.getItem('search_college')) {
      this.college = sessionStorage.getItem('search_college')
    }
    if (sessionStorage.getItem('search_continent') === 'northamerica') {
      this.continentclick_1()
    } else if (sessionStorage.getItem('search_continent') === 'europe') {
      this.continentclick_2()
    } else if (sessionStorage.getItem('search_continent') === 'asia') {
      this.continentclick_3()
    } else if (sessionStorage.getItem('search_continent') === 'oceania') {
      this.continentclick_4()
    } else if (sessionStorage.getItem('search_continent') === 'northamerica') {
      this.continentclick_5()
    } else {
      this.getData()
    }
  },
  unmounted() {},
  watch: {
    continent_name: function (value) {
      sessionStorage.setItem('search_continent', value)
    },
    weather: function (value) {
      sessionStorage.setItem('search_weather', value)
    },
    language: function (value) {
      sessionStorage.setItem('search_language', value)
    },
    dormitory: function (value) {
      sessionStorage.setItem('search_dormitory', value)
    },
    order: function (value) {
      sessionStorage.setItem('search_order', value)
    },
    college: function (value) {
      sessionStorage.setItem('search_college', value)
    }
  },
  computed: {
    heightchange() {
      if (this.seperated_univ2[this.present_page - 1].length >= 4) {
        return 1415
      } else if (this.seperated_univ2[this.present_page - 1].length >= 3) {
        return 1060
      } else if (this.seperated_univ2[this.present_page - 1].length >= 2) {
        return 705
      } else if (this.seperated_univ2[this.present_page - 1].length >= 1) {
        return 355
      } else {
        return 20
      }
    },
    total_page() {
      if (this.number > 84) {
        return 8
      } else if (this.number > 72) {
        return 7
      } else if (this.number > 60) {
        return 6
      } else if (this.number > 48) {
        return 5
      } else if (this.number > 36) {
        return 4
      } else if (this.number > 24) {
        return 3
      } else if (this.number > 12) {
        return 2
      } else if (this.number > 0) {
        return 1
      } else {
        return 0
      }
    },
    sel() {
      if (this.search_name === '') {
        return false
      } else {
        return true
      }
    },
    sel1() {
      if (this.continent_name === '') {
        return false
      } else {
        return true
      }
    },
    sel2() {
      if (this.weather === '') {
        return false
      } else {
        return true
      }
    },
    sel3() {
      if (this.language === '') {
        return false
      } else {
        return true
      }
    },
    sel4() {
      if (this.dormitory === '') {
        return false
      } else {
        return true
      }
    },
    sel5() {
      if (this.order === '') {
        return false
      } else {
        return true
      }
    },
    con() {
      return [this.sel, this.sel1, this.sel2, this.sel3, this.sel4, this.sel5]
    }
  },
  methods: {
    continentclick_1() {
      if (this.continent_clicks === false) {
        this.continent_name = 'northamerica'
        this.continent_clicked[0] = !this.continent_clicked[0]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      } else if (this.continent_clicks === true) {
        this.continent_name = ''
        this.continent_clicked[0] = !this.continent_clicked[0]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      }
    },
    continentclick_2() {
      if (this.continent_clicks === false) {
        this.continent_name = 'europe'
        this.continent_clicked[1] = !this.continent_clicked[1]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      } else if (this.continent_clicks === true) {
        this.continent_name = ''
        this.continent_clicked[1] = !this.continent_clicked[1]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      }
    },
    continentclick_3() {
      if (this.continent_clicks === false) {
        this.continent_name = 'asia'
        this.continent_clicked[2] = !this.continent_clicked[2]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      } else if (this.continent_clicks === true) {
        this.continent_name = ''
        this.continent_clicked[2] = !this.continent_clicked[2]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      }
    },
    continentclick_4() {
      if (this.continent_clicks === false) {
        this.continent_name = 'oceania'
        this.continent_clicked[3] = !this.continent_clicked[3]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      } else if (this.continent_clicks === true) {
        this.continent_name = ''
        this.continent_clicked[3] = !this.continent_clicked[3]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      }
    },
    continentclick_5() {
      if (this.continent_clicks === false) {
        this.continent_name = 'southamerica'
        this.continent_clicked[4] = !this.continent_clicked[4]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      } else if (this.continent_clicks === true) {
        this.continent_name = ''
        this.continent_clicked[4] = !this.continent_clicked[4]
        this.continent_clicks = !this.continent_clicks
        this.present_page = 1
        this.getData()
      }
    },
    ranking() {
      this.detailsearch_clicked[0] = !this.detailsearch_clicked[0]
    },
    transportation() {
      this.detailsearch_clicked[1] = !this.detailsearch_clicked[1]
    },
    money() {
      this.detailsearch_clicked[2] = !this.detailsearch_clicked[2]
    },
    case1() {
      this.present_page = 1
    },
    case2() {
      this.present_page = 1
    },
    async getData() {
      try {
        const res = await axios.get('/api/detailsearch', {
          params: {
            name: this.search_name,
            continent: this.continent_name,
            weather: this.weather,
            language: this.language,
            domi: this.dormitory,
            order: this.order,
            condition: this.con,
            college: this.college
          }
        })
        if (res.data.length === 0) {
          this.seperated_univ2 = [[], [], [], [], [], [], [], []]
          this.number = 0
        } else {
          this.isLoading = true
          this.selected_univ = res.data
          this.number = this.selected_univ.length
          for (let i = 0; i < Math.ceil(this.number / 3); i++) {
            this.seperated_univ.push(this.selected_univ.slice(0, 3))
            this.selected_univ.splice(0, 3)
          }
          for (let j = 0; j < Math.ceil(this.number / 12); j++) {
            this.seperated_univ2[j] = this.seperated_univ.slice(0, 4)
            this.seperated_univ.splice(0, 4)
          }
        }
      } catch (err) {
        console.error(err)
      }
    },
    page_up() {
      if (this.present_page < this.total_page) {
        this.present_page += 1
      }
    },
    page_down() {
      if (this.present_page !== 1) {
        this.present_page -= 1
      }
    },
    detailresult(event) {
      this.$router.push({
        name: 'detailresult',
        query: { name: event.target.value }
      })
    },
    Update() {
      this.getData()
      this.present_page = 1
    }
  }
}
</script>
<style scoped>
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  display: flex;
  flex-direction: column;
  font-family: Inter;
}
.intro_box {
  width: 1440px;
  height: 300px;
  z-index: 2;
  display: flex;
  flex-direction: column;
  margin-left: 10%;
  margin-top: 3%;
  font-family: Inter;
}
.intro_msg {
  margin-left: 8%;
}
.search_msg {
  margin-left: 8%;
  color: gray;
}
.search_box {
  width: 1440px;
  height: 100px;
  display: flex;
  margin-top: 60px;
}
.search {
  box-shadow: 0px 2px 15px rgb(0 0 0 / 25%);
  background-color: rgba(255, 255, 255, 1);
  width: 1100px;
  height: 80px;
  margin-left: 155px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-left-radius: 50px;
  border-bottom-right-radius: 50px;
  font-size: 40px;
  border: 0;
  outline: 0;
  text-align: center;
}
.search_button {
  border: 0;
  outline: 0;
  background-image: url(../assets/find.png);
  background-size: cover;
  width: 60px;
  height: 60px;
  background-color: transparent;
  top: 395px;
  left: 1175px;
  position: absolute;
}
.continent_box {
  width: 1440px;
  height: 210px;
  display: flex;
  margin-top: 60px;
  padding-bottom: 10px;
  border-bottom: 10px solid #d3d3d3;
}
.continent_box_samll {
  display: block;
  height: 210px;
  width: 216px;
}
.continent_box_samll.first {
  margin-left: 180px;
}
.continent_img_circle {
  border-radius: 30px;
  background-color: rgba(
    217.0000022649765,
    217.0000022649765,
    217.0000022649765,
    1
  );
  width: 156px;
  height: 156px;
  margin-top: 3%;
  background-size: cover;
  border: 3px solid black;
  outline: 0;
  margin-left: 30px;
}
.continent_img_circle.northamerica {
  background-image: url(../assets/northamerica.png);
}
.continent_img_circle.northamerica.clicked {
  background-color: gray;
}
.continent_img_circle.europe {
  background-image: url(../assets/europe.png);
}
.continent_img_circle.europe.clicked {
  background-color: gray;
}
.continent_img_circle.asia {
  background-image: url(../assets/asia.png);
}
.continent_img_circle.asia.clicked {
  background-color: gray;
}
.continent_img_circle.oceania {
  background-image: url(../assets/oceania.png);
}
.continent_img_circle.oceania.clicked {
  background-color: gray;
}
.continent_img_circle.southamerica {
  background-image: url(../assets/southamerica.png);
}
.continent_img_circle.southamerica.clicked {
  background-color: gray;
}
.continent_msg {
  font-size: 20px;
  font-weight: bold;
  margin-top: 3%;
  text-align: center;
}
.detailsearch_box {
  width: 1440px;
  height: 100px;
  display: flex;
  border-bottom: 10px solid #d3d3d3;
}
.detailsearch_dropdown_box {
  height: 100px;
}
.detailsearch_dropdown_box.first {
  width: 163.5px;
  margin-left: 211.25px;
}
.detailsearch_dropdown_box.second {
  width: 110px;
  margin-left: 50px;
}
.detailsearch_dropdown_box.third {
  width: 109.5px;
  margin-left: 50px;
}
.detailsearch_dropdown_box.fourth {
  width: 136.5px;
  margin-left: 50px;
}
.detailsearch_dropdown_box.fifth {
  width: 148px;
  margin-left: 50px;
}
.detailsearch_dropdown_box.sixth {
  width: 50px;
  margin-left: 100px;
}
.detailsearch_dropdown {
  height: 50px;
  border-radius: 100px;
  padding: 5px;
  margin-top: 25px;
  color: black;
  text-align-last: center;
  text-align: center;
}
.dropdown_option {
  padding-left: 50px;
}
.detailsearch_button {
  border-radius: 100px;
  border: 2px solid black;
  height: 50px;
  margin-top: 25px;
  margin-left: 30px;
  background-color: white;
  color: black;
}
.detailsearch_button.ranking {
  margin-left: 33px;
}
.detailsearch_button.transportation {
  margin-left: 0px;
}
.detailsearch_button.money {
  margin-left: 28.89px;
}
.detailsearch_button.ranking.clicked {
  background-color: #d3d3d3;
}
.detailsearch_button.transportation.clicked {
  background-color: #d3d3d3;
}
.detailsearch_button.money.clicked {
  background-color: #d3d3d3;
}
.search_button_2 {
  width: 50px;
  height: 50px;
  margin-top: 20px;
  background-size: cover;
  background-image: url(../assets/find.png);
  border: 0;
  outline: 0;
  background-color: transparent;
}
.univlist_box {
  display: flex;
  width: 1440px;
  height: 305px;
  padding-top: 50px;
}
.univ_box {
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 330px;
  height: 305px;
  margin-left: 112.5px;
  border-radius: 20px;
}
.univimg_box {
  background-repeat: no-repeat;
  background-size: cover;
  width: 300px;
  height: 190px;
  margin-left: 15px;
  margin-top: 30px;
  border: 0;
  outline: 0;
  border-radius: 10px;
}
.univ_name {
  color: rgba(0, 0, 0, 1);
  width: 300px;
  height: 36.5px;
  font-family: Inter;
  text-align: left;
  font-size: 17px;
  letter-spacing: 0;
  padding-left: 20px;
  padding-top: 10px;
}
.univ_country {
  color: rgba(93.50000202655792, 93.50000202655792, 93.50000202655792, 1);
  width: 330px;
  height: 36.5px;
  font-family: Inter;
  text-align: left;
  font-size: 14px;
  letter-spacing: 0;
  padding-left: 20px;
}
.page_number_box {
  width: 1440px;
  height: 70px;
  margin-top: 30px;
}
.page_number_container {
  width: 140px;
  height: 40px;
  border-radius: 100px;
  margin-left: 650px;
  border: 1px solid black;
  margin-top: 50px;
  display: flex;
  box-shadow: 0px 2px 15px rgb(0 0 0 / 25%);
}
.page_number {
  font-size: 26px;
  font-weight: bold;
  width: 36px;
  margin-left: 20px;
  margin-top: 4px;
}
.right_arrow {
  width: 28px;
  height: 28px;
  margin-left: 18px;
  border: 0;
  outline: 0;
  margin-top: 6px;
  padding: 0px;
  font-size: 20px;
  background-color: transparent;
  font-weight: bold;
}
.left_arrow {
  width: 28px;
  height: 28px;
  border: 0;
  outline: 0;
  margin-top: 6px;
  margin-left: 6px;
  padding: 0px;
  font-size: 20px;
  background-color: transparent;
  font-weight: bold;
}
.load {
  margin-left: 45%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 800px;
  height: 72px;
  font-size: 45px;
  letter-spacing: 0;
  flex-shrink: 1;
  font-family: Inter;
}
.intro_msg2 {
  color: gba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 600px;
  height: 30px;
  font-family: Inter;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
</style>
