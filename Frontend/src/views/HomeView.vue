<template>
  <div class="container">
    <div class="intro">
      <div class="intro_msg">한번뿐인 교환학생 <br>어디로 떠날까?</div>
      <div class="box">
        <router-link to="/worldmap">
          <span class="box_msg">비행기 타러 출발! ✈️</span>
        </router-link>
      </div>
    </div>
    <div class="passport"></div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
* {
  font-family: Inter;
}
.container {
  overflow: hidden;
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  height: 350px;
  display: flex;
  flex-direction: row;
  margin-top: 10%;
  margin-bottom: 5%;
}
.box {
  background-color: rgba(18, 24, 40, 1);
  width: 340px;
  height: 90px;
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  margin-top: 30%;
}
.box_msg {
  color: white;
  font-family: Inter;
  font-size: 32px;
  margin-left: 30px;
  margin-top: 18px;
  position: absolute;
}
.passport {
  width: 560px;
  height: 480px;
  background-image: url(../assets/passport.png);
  background-repeat: no-repeat;
  background-size: cover;
  margin-left: 12%;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-left: 10%;
  align-items: center;
}
.intro_msg {
  color: rgba(0, 0, 0, 1);
  width: 600px;
  height: 100px;
  font-family: Inter;
  text-align: left;
  font-size: 64px;
  letter-spacing: 0;
}
a {
  text-decoration-line: none;
}
</style>
