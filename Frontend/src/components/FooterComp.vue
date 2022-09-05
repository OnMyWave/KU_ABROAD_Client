<template>
  <footer>
    <div class="bar"></div>
    <div class="content-info">
      <div class="logo">&nbsp;&nbsp;&nbsp;&nbsp;KU ABROAD</div>
      <div class="info">
        <ul>
          <li class="li_item"><router-link to="/"><span class="msg"></span>Home</router-link></li>
          <li class="li_item"><router-link to="intro"><span class="msg"></span>팀원 소개</router-link></li>
          <li class="li_item a"><a href="https://studyabroad.korea.ac.kr/studyabroad/index.do">고려대학교<br>국제처</a></li>
          <li class="li_item a"><a href="https://ic.korea.ac.kr/ic/index.do">Data@KU</a></li>
        </ul>
      </div>
      <div class="icon_container">
        <div class="icon"></div>
        <div class="icon_3"></div>
        <div class="icon_2"></div>
      </div>
    </div>
    <div class="copyright">
      <span class="copyright_str"
        >© 2022 KU Datathon. All Rights Reserved.</span
      >
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      footerInfo: [
        'Home',
        'About Us',
        'Pricing',
        'Features',
        'Contact',
        'Terms',
        'Privacy'
      ]
    }
  },
  method: {}
}
</script>

<style scoped>
* {
  font-family: Inter;
}
a {
  text-decoration-line: none;
  color: black;
}
footer {
  width: 1440px;
  height: 180px;
  position: absolute;
  left: 0%;
  bottom: 5%;
  display: flex;
  flex-direction: column;
}
.content-info {
  width: 100%;
  margin: 10px auto;
  display: inline-block;
}
.logo {
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  margin-left: 10%;
  margin-right: 15%;
  background-color: rgba(255, 255, 255, 1);
  width: 50px;
  height: 40px;
  color: black;
  font-weight: bold;
  font-size: 20px;
  text-align: center;
  float: left;
}
.info {
  margin-left: 25%;
  margin-right: 5%;
  flex-direction: row;
  justify-content: space-between;
}
.icon_container {
  width: 10%;
  float: right;
  margin-right: 10%;
}
.icon {
  background-image: url(../assets/footer_logo/logo_1.png);
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
  margin-right: 10%;
  float: right;
}
.icon_2 {
  background-image: url(../assets/footer_logo/logo_2.png);
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
  margin-right: 10%;
  float: right;
}
.icon_3 {
  background-image: url(../assets/footer_logo/logo_3.png);
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
  margin-right: 10%;
  float: right;
}
.bar {
  background-color: rgba(210, 210, 210);
  width: 960px;
  height: 1px;
  margin: auto;
  top: 10px;
}
.li_item {
  color: rgba(75.00000312924385, 85.0000025331974, 99.00000169873238, 1);
  width: 80px;
  height: 32px;
  left: 4px;
  top: 4px;
  text-align: center;
  font-size: 16px;
  list-style-type: none;
  float: left;
  margin-left: 60px;
}
.li_item.a{
  width: 120px;
  height: 18px;
}
.copyright {
  width: 30%;
  text-align: center;
  margin-left: 35%;
  margin-top: 20px;
}
.copyright_str {
  text-align: center;
  margin: 10%, 30%, 30%, 10%;
}
</style>
