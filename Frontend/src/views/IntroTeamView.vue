<template>
<div class="container">
    <div class="intro">
      <span class="intro_msg1">About Us ..</span>
    </div>
    <div class="person_box">
      <div class="person_img_box">
        <div class="person_img"></div>
      </div>
        <div class="person_msg">
          <div class="name">이종근</div>
          <div class="info">고려대학교 산업경영공학부 19학번</div>
          <div class="job">데이터 분석 및 웹 개발 (Frontend / Backend)</div>
          <div class="msg">금융공학과 시스템 최적화에 관심있는 개발자입니다.</div>
          <div class="contact">Contact : onmywave@kakao.com</div>
        </div>
    </div>
     <div class="person_box">
      <div class="person_img_box">
        <div class="person_img a"></div>
      </div>
        <div class="person_msg">
          <div class="name">김민수</div>
          <div class="info">고려대학교 산업경영공학부 19학번</div>
          <div class="job">웹 개발 (Frontend / Backend)</div>
          <div class="msg">금융과 교육에 관심이 많은 개발자 꿈나무입니다.</div>
          <div class="contact">Contact : hn7080@naver.com</div>
        </div>
    </div>
     <div class="person_box">
      <div class="person_img_box">
        <div class="person_img b"></div>
      </div>
        <div class="person_msg">
          <div class="name">최진성</div>
          <div class="info">고려대학교 산업경영공학부 19학번</div>
          <div class="job">데이터 분석 및 개발</div>
          <div class="msg">데이터 중심의 과학발전사회를 위해 공부하고 있는, <br> 미래의 대통령을 꿈꾸는 청춘입니다.</div>
          <div class="contact">Contact : eric914choi@naver.com</div>
        </div>
    </div>
     <div class="person_box">
      <div class="person_img_box">
        <div class="person_img c"></div>
      </div>
        <div class="person_msg">
          <div class="name">오지수</div>
          <div class="info">고려대학교 경영학과 20학번</div>
          <div class="job">기획 및 디자인</div>
          <div class="msg">MIS와 Tech를 이용해 스타트업 생태계를 이끌어가고 싶은 경영학도입니다.</div>
          <div class="contact">Contact : jisoosummeroh@gmail.com</div>
        </div>
    </div>
     <div class="person_box">
      <div class="person_img_box">
        <div class="person_img d"></div>
      </div>
        <div class="person_msg">
          <div class="name">천유진</div>
          <div class="info">고려대학교 경영학과 20학번</div>
          <div class="job">기획 및 데이터 수집</div>
          <div class="msg">경제와 데이터 분석에 관심이 많은 경영학도입니다.</div>
          <div class="contact">Contact : jenny_1000@naver.com</div>
        </div>
    </div>
 </div>
</template>
<script>
export default {
    components: {},
    data() {
        return {
            sampleData:''
        }
    },
    setup() {},
    created() {},
    mounted() {},
    unmounted() {},
    methods:{}
}
</script>
<style scoped>
.contact {
  margin-top: 3%;
  color: gray;
}
.info {
  color: rgb(71, 69, 69);
  margin-bottom: 3%;
}
.msg {
  margin-top: 5%;
  width: 500px;

}
.job {
  color: gray;
  font-size: 20px;
}
.name{
  font-size: 30px;
  margin-bottom: 1%;
}
.img_binder {
    width: 200px;
    height: 200px;
}
.person_img_box {
  margin-left: 5%;
  margin-right: 5%;
}
.person_img {
  width: 200px;
  height: 200px;
  border-top-left-radius: 82.5px;
  border-top-right-radius: 82.5px;
  border-bottom-left-radius: 82.5px;
  border-bottom-right-radius: 82.5px;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url('https://avatars.githubusercontent.com/u/63710797?s=400&u=cfe182e427dbe20fe4e4a2989212cbcd4dc70bec&v=4');
  margin-bottom: 10%;
}
.person_img.a {
  background-image: url(../assets/minsu.png);
}
.person_img.b {
  background-image: url(../assets/jinsung.jpeg);
}
.person_img.c {
  background-image: url(../assets/jisu.png);
}
.person_img.d{
  background-image: url(../assets/yujin.jpeg);
}
.person_msg {
    width: 800px;
    height: 200px;
    margin-left: 5%;
}
.container {
  background-color: rgba(255, 255, 255, 1);
  width: 1440px;
  display: flex;
  flex-direction: column;
  justify-content:  center;
  align-items : center;
}
.intro {
  display: flex;
  flex-direction: column;
  margin-top: 3%;
  margin-left: 25%;
}
.intro_msg1 {
  color: rgba(0, 0, 0, 1);
  width: 1440px;
  height: 58px;
  font-family: Inter;
  text-align: left;
  font-size: 44.86062240600586px;
  margin-top: 10px;
  letter-spacing: 0;
}
.intro_msg2 {
  color: rgba(153.00000607967377, 153.00000607967377, 153.00000607967377, 1);
  width: 745px;
  height: 43px;
  font-family: Inter;
  text-align: left;
  margin-top: 10px;
  font-size: 22.101093292236328px;
  letter-spacing: 0;
}
.person_box {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 1);
  width: 918px;
  height: 350px;
  display: flex;
  flex-direction: row;
  margin-top: 3%;
  justify-content :center;
  align-items: center;
}
</style>