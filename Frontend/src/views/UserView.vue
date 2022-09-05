<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1">추천을 위한 기본적인 정보를 알려주세요.</span>
      <span class="intro_msg2"
        >해당 정보는 저장되지 않으며, 추천을 위한 알고리즘에만 사용됩니다
      </span>
    </div>
    <div class="boxwrapper">
      <div class="box">
        <span class="title">파견을 원하는 학기</span>
        <select v-model="semester" class="select">
          <option disabled value="">학기를 선택해주세요</option>
          <option value="1">1학기</option>
          <option value="2">2학기</option>
        </select>
      </div>
      <div class="box">
        <span class="title">소속 단과대학</span>
        <select v-model="college" class="select">
          <option disabled value="">단과대학을 선택해주세요</option>
          <option value="h">인문대학</option>
          <option value="m">정경대학</option>
          <option value="t">공과대학</option>
          <option value="n">자연대학</option>
          <option value="l">생명과학대학</option>
        </select>
      </div>
      <div class="box">
        <span class="title">학년</span>
        <select v-model="department" class="select">
          <option disabled value="">학년을 선택해주세요</option>
          <option>1학년</option>
          <option>2학년</option>
          <option>3학년</option>
          <option>4학년</option>
        </select>
      </div>
    </div>
    <button
      @click="next"
      :class="{
        clicked:
          semester.length > 0 && college.length > 0 && department.length > 0,
        clicked_1: semester === '' || college === '' || department === ''
      }"
      :disabled="semester === '' || college === '' || department === ''"
    >
      다음 단계로 넘어가기
    </button>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      semester: '',
      department: '',
      college: ''
    }
  },
  setup() {},
  create() {},
  mounted() {},
  unmounted() {},
  methods: {
    next() {
      sessionStorage.setItem('semester', this.semester)
      sessionStorage.setItem('college', this.college)
      this.$router.push('select')
      sessionStorage.setItem('recommended', 'false')
    }
  }
}
</script>
<style scoped>
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 400px;
  display: flex;
  flex-direction: column;
  margin-top: 50px;
  margin-bottom: 7%;
}
.box {
  width: 320px;
  height: 280px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-bottom: 10%;
}
.boxwrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 3%;
  margin-bottom: 5%;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  margin-left: 10%;
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

.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 1000px;
  height: 58px;
  font-family: Inter;
  text-align: left;
  font-size: 44.86062240600586px;
  letter-spacing: 0;
}
.title {
  color: rgba(0, 0, 0, 1);
  width: 250px;
  height: 33px;
  font-family: Inter;
  text-align: left;
  font-size: 25.72804069519043px;
  letter-spacing: 0;
  margin-bottom: 10%;
}
.select {
  width: 280px;
  height: 60px;
}
.clicked_1 {
  background-color: gray;
  width: 270px;
  height: 64.79875946044922px;
  position: absolute;
  left: 560px;
  top: 800px;
  border-top-left-radius: 21.362228393554688px;
  border-top-right-radius: 21.362228393554688px;
  border-bottom-left-radius: 21.362228393554688px;
  border-bottom-right-radius: 21.362228393554688px;
  font-size: 25px;
  font-weight: bold;
  color: white;
  border: 3px solid black;
  outline: 0;
}
.clicked {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 270px;
  height: 64.79875946044922px;
  position: absolute;
  left: 560px;
  top: 800px;
  border-top-left-radius: 21.362228393554688px;
  border-top-right-radius: 21.362228393554688px;
  border-bottom-left-radius: 21.362228393554688px;
  border-bottom-right-radius: 21.362228393554688px;
  font-size: 25px;
  font-weight: bold;
  color: white;
  border: 3px solid black;
  outline: 0;
}
a {
  text-decoration-line: none;
}
</style>
