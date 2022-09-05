<template >
  <header>
    <div class="wrapper">
      <div class="logo">
        <router-link to="/"
          ><span class="logo_color"
            >&nbsp;&nbsp;&nbsp;&nbsp;KU ABROAD</span
          ></router-link
        >
      </div>
      <nav>
        <ul>
          <span class="li_item"><router-link to="intro">팀원 소개</router-link></span>
          <span class="li_item"><router-link to="plot">Univ-Map</router-link></span>
          <span class="li_item"><router-link to="alluniv">전체 보기</router-link></span>
        </ul>
      </nav>
    </div>
    <div class="bar"></div>
  </header>
</template>
<script>
export default {
  data() {
    return {
      headerInfo: ['학교 추천', 'World Map', '프로젝트 소개']
    }
  }
}
</script>

<style scoped>
* {
  font-family: Inter;
}
header {
  width: 1440px;
  height: 165px;
  justify-content: space-between;
  flex-direction: column;
  top: 5%;
  display: block;
  left: 0;
  right: 0;
}
.wrapper {
  width: 1440px;
  height: 155px;
}
.logo {
  font-family: Inter;
  margin-top: 3%;
  margin-left: 10%;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  height: 40px;
  float: left;
  width: 100px;
  color: black;
  font-weight: bold;
  font-size: 30px;
}
.logo_color {
  color: black;
}
.li_item {
  color: rgba(75.00000312924385, 85.0000025331974, 99.00000169873238, 1);
  width: 100px;
  height: 18px;
  font-family: Inter;
  text-align: left;
  font-size: 18px;
  letter-spacing: 0;
  list-style-type: none;
  float: right;
  margin-right: 40px;
  margin-top: 5%;
}
.bar {
  background-color: rgba(210, 210, 210);
  width: 960px;
  height: 1px;
  margin: auto;
}
a {
  text-decoration-line: none;
  color: black;
}
</style>
