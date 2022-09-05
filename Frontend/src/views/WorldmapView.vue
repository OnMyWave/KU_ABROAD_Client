<template>
  <div class="container">
    <div class="intro">
      <span class="intro_msg1">떠나고 싶은 지역이 있나요?</span>
      <span class="intro_msg2">가고 싶은 지역을 누르면 선택됩니다.</span>
    </div>
    <div class="world"></div>
    <button @click="next" value="southamerica" class="namerica">남미</button>
    <button @click="next" value="northamerica" class="samerica">북미</button>
    <button @click="next" value="oceania" class="oceania">오세아니아</button>
    <button @click="next" value="asia" class="asia">아시아</button>
    <button @click="next" value="europe" class="europe">유럽</button>
    <button @click="next" value="none" class="empty">
      아직 선택이 어려워요💦
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countryname: ''
    }
  },
  methods: {
    next(event) {
      this.countryname = event.target.value
      sessionStorage.setItem('country', this.countryname)
      this.$router.push('user')
      sessionStorage.setItem('recommended', 'false')
    }
  }
}
</script>

<style scoped>
.container {
  overflow: auto;
  width: 1440px;
  height: 700px;
  display: flex;
  flex-direction: column;
}
.world {
  background-color: rgba(255, 255, 255, 1);
  width: 1200px;
  height: 720px;
  z-index: 1;
  margin-top: 5%;
}
.intro {
  z-index: 2;
  display: flex;
  flex-direction: column;
  margin-left: 10%;
  margin-top: 3%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 1000px;
  height: 72px;
  font-size: 45px;
  letter-spacing: 0;
  flex-shrink: 1;
}
.intro_msg2 {
  color: gba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 420px;
  height: 30px;
  font-family: Inter;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
.empty {
  background-color: rgba(
    41.43749848008156,
    41.43749848008156,
    41.43749848008156,
    1
  );
  width: 250px;
  height: 64.79875946044922px;
  position: absolute;
  left: 592px;
  top: 950px;
  border-top-left-radius: 21.362228393554688px;
  border-top-right-radius: 21.362228393554688px;
  border-bottom-left-radius: 21.362228393554688px;
  border-bottom-right-radius: 21.362228393554688px;
  color: white;
  font-size: 20px;
  z-index: 2;
  border: 0;
  outline: 0;
}
.world {
  width: 1200px;
  height: 620px;
  position: absolute;
  left: 120px;
  top: 275px;
  background-image: url(../assets/map.png);
  background-repeat: no-repeat;
  background-size: cover;
}
.namerica {
  background-color: aliceblue;
  width: 101px;
  height: 56.999996185302734px;
  position: absolute;
  left: 438px;
  top: 800px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 25px;
  font-weight: bold;
  z-index: 2;
  border: 3px solid black;
  outline: 0;
  color: black;
}
.samerica {
  background-color: aliceblue;
  width: 108.99999237060547px;
  height: 56.000003814697266px;
  position: absolute;
  left: 300px;
  top: 580px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 25px;
  font-weight: bold;
  z-index: 2;
  border: 3px solid black;
  outline: 0;
  color: black;
}
.oceania {
  background-color: aliceblue;
  width: 110px;
  height: 50px;
  position: absolute;
  left: 1080px;
  top: 800px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 18px;
  font-weight: bold;
  z-index: 2;
  border: 3px solid black;
  outline: 0;
  color: black;
}
.asia {
  background-color: aliceblue;
  width: 124px;
  height: 48px;
  position: absolute;
  left: 970px;
  top: 540px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 25px;
  font-weight: bold;
  z-index: 2;
  border: 3px solid black;
  outline: 0;
  color: black;
}
.europe {
  background-color: aliceblue;
  width: 103.99999237060547px;
  height: 55px;
  position: absolute;
  left: 725px;
  top: 550px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  font-size: 25px;
  font-weight: bold;
  z-index: 2;
  border: 3px solid black;
  outline: 0;
  color: black;
}
a {
  text-decoration-line: none;
}
</style>
