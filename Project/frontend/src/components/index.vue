<template>
  <v-app>
    <v-carousel height="400px" hide-delimiters>
        <v-carousel-item
            v-for="(imageSrc, i) in carouselImages"
            :key="i"
            :src="imageSrc"
        ></v-carousel-item>
    </v-carousel>
    <v-stepper v-if="isLogin && dataExist === true" class="" style="background-color:#C5D6FF;">
        <v-stepper-content step="1" class="pt-1">
          <v-card
            class="my-6"
            color="brown lighten-5"
            min-width="300"
          >
            <v-card-text
              class="px-4 text-center"
            > 
              <v-card
                class="mx-auto"
                max-width="400"
              >
                <v-toolbar
                  color="blue darken-3"
                  dark
                > 
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">{{ userNickname }}님의 최근 성적통지표</v-col>
                </v-toolbar>
                <v-row style="margin: auto;">
                  <v-col cols="3" 
                    class="pb-0 pl-0 pr-0 pt-0" 
                    style="border-top-style: solid; border-top-color: white; 
                          border-bottom-style: solid; border-bottom-color: white; color: white;
                          border-right-style: solid;
                          border-right-color:white;"
                  >

                    <v-img 
                      :src="recentImage" 
                      cover
                      style="cursor:pointer;"
                      min-width="64px"
                      max-height="95px"
                      height="100%"
                    ></v-img>  

                  </v-col>
                  <v-col cols="9" class="pb-0 pl-0 pr-0 pt-0">
                    <v-row style="margin: auto; background-color: gray;">
                      <v-col 
                        class="resultText" 
                        style="border-top-style: solid; border-top-color: white; border-bottom-style: solid; border-bottom-color: white; color: white;">
                        닉네임
                      </v-col>
                    </v-row>
                    <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                      <v-col class="resultText" style="background-color: lightgray;">{{ userNickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">구분</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">정수리 영역</v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">점수</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ userScore }} 점</v-col>
                </v-row>
                <v-row style="margin: auto;">
                  <v-col cols="3" class="resultBorder">등급</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ userGrade }} 등급</v-col>
                </v-row>
              </v-card>
              <v-row>
                <v-col class="pb-0 pt-5" style="font-family: 'Jua', sans-serif; font-size: large;">{{ this.userDate }}</v-col>
              </v-row>
              <v-row class="mb-5">
                <v-col class="pt-0" style="font-family: 'Jua', sans-serif; font-size: large;">정수리영역평가원장</v-col>
              </v-row>
              <v-row v-if="userGrade < 4" class="gradeResult1 text-left" style="margin: auto;">                
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">3등급 이하</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">아직 안전한 단계</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large; color: white">두피를 청결하게 유지</span>
                  <span style="font-size: large;">하고 좋은 생활 습관을 통해 탈모를 예방하세요.</span>
                </v-col>
              </v-row>
              <v-row v-else-if="userGrade < 7" class="gradeResult2 text-left" style="margin: auto;"> 
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">4~7등급</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">탈모 초기 증상</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large;">빨리 전문적인 진료를 받아 </span>  
                  <span style="font-size: large; color: white">적극적인 탈모/투피 치료</span>
                  <span style="font-size: large;">를 받으셔야 조기 예방, 개선할 수 있습니다.</span>
                </v-col>
              </v-row>
              <v-row v-else-if="userGrade < 10" class="gradeResult3 text-left" style="margin: auto;">
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">7등급 이상</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">탈모 진행 중</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large;">정확한 진단 후 </span>
                  <span style="font-size: large; color: white">탈모 전문 치료</span>
                  <span style="font-size: large;">를 받으셔야 더 이상의 악화 현상을 받지할 수 있습니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-stepper-content>
    </v-stepper>
    <div v-else>
    <v-img src="@/static/index/main0.png" width="100%" height="100%" cover/>
    </div>
</v-app>
</template>

<script>
import { checkLogin } from '@/utils/index';
import { getUserInfo } from '@/api/index';

export default {
    name : 'index',
    data() {
        return {
            carouselImages : [
                require('@/static/index/main1.png'),
                require('@/static/index/main2.png'),
                require('@/static/index/main3.png'),
                require('@/static/index/main4.png'),
                require('@/static/index/main5.png'),
            ],
            mainImage : require("@/static/index/main0.png"),
            dataExist : false,
            userNickname : null,
            userDate : null,
            userScore : null,
            userGrade : null,
            recentImage : null,
        }
    },
    computed : {
        isLogin() {
            return checkLogin();
        },
    },
    methods : {

    },
    async created() {
        if (this.isLogin) {
            const response = await getUserInfo(sessionStorage.getItem('token'));
            const data = response.data;
            const images = data.images.filter(x => x.score !== 0);

            if (images.length) {
                this.dataExist = true;
                const recentData = images.slice(-1)[0];
                this.userNickname = recentData.upload_user.nickname;
                this.userScore = recentData.score;
                if (this.userScore == 100) {
                this.userGrade = 1
                } else {
                this.userGrade = 10 - parseInt(this.userScore / 10)
                }
                this.recentImage = process.env.VUE_APP_BACKEND_URL + recentData.upload_image;

                let uploadDate = new Date(recentData.upload_date);
                let year = uploadDate.getFullYear()
                let month = uploadDate.getMonth() + 1
                let date = uploadDate.getDate()
                this.userDate = `${year}.${month}.${date}`
            } else {
                this.dataExist = false;
            }
        }
    },
    components : {

    },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR&family=Do+Hyeon&family=Nanum+Gothic&family=Noto+Sans+KR:wght@900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

.surbeyHighlight {
  color:#FFAB00;
  font-family: 'Do Hyeon', sans-serif;

}

.surbeyNomal {
  font-family: 'Do Hyeon', sans-serif;
}

.surbeyTitle {
font-family: 'Noto Sans KR', sans-serif;
font-weight: 900;
}

.testSample {
  border: 3px solid gold;
  border-radius: 220px;
  -moz-border-radius: 220px;
  -khtml-border-radius: 220px;
  -webkit-border-radius: 220px;
}

.resultBorder {
  margin: auto;
  border-right-style: solid;
  border-right-color:white;
  width: 20px !important;
  background-color: gray;
  color: white;
  font-family: 'Jua', sans-serif;
  font-size: large
}

.resultText {
  font-family: 'Jua', sans-serif;
  font-size: large;
}

.gradeResult1 {
  background-color: #ffbe73;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.gradeResult2 {
  background-color: #fd9463;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.gradeResult3 {
  background-color: #ff5953;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.v-progress-circular {
  margin: 1rem;
}

.v-progress-circular__info {
  /* color: rgb(0, 16, 85); */
  color: white;
  font-weight: 550;
  font-size: xx-large;
  font-family: 'Jua', sans-serif;
}
</style>