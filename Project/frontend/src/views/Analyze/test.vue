<template>
  <v-container>
    <v-stepper v-model="e1" alt-labels class="d-flex flex-column justify-space-between align-center mt-1">
      <h3 v-if="this.e1 == 1" class="pt-2">쉿🤐..정수리 시험 중..!!</h3>
      <h3 v-else class="pt-2">정수리 시험 점수는..✨😲</h3>
      <v-stepper-items>
        <v-stepper-content step="1" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">AI 카메라 (1/1)</div>
          <!-- 사진 업로드 안했을 때 -->
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="!imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center" class="mx-0">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <input ref="imageInput" type="file" hidden @change="onChangeImages">
                  <v-img
                    src="../../assets/11.png"
                    class="testSample"
                    @click="onClickImageUpload"
                    style="cursor:pointer;"
                    width="200px"
                  ></v-img>                   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large;">이미지를 업로드해주세요</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="!imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              disabled
            >
              다음
            </v-btn>
          </div>

          <!-- 사진 업로드 후 -->
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <v-img 
                    :src="imageUrl" 
                    cover
                    @click="onClickImageUpload" 
                    style="cursor:pointer;"
                    width="200px"
                  >
                  </v-img>
                  <input ref="imageInput" type="file" hidden @change="onChangeImages">               
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large">이미지를 업로드해주세요.</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              @click="upload"
            >
              다음
            </v-btn>
          </div>
        </v-stepper-content>


        <v-stepper-content step="2" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">채점중..</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <v-img 
                    :src="imageUrl" 
                    cover
                    style="cursor:pointer;"
                    width="200px"
                  >
                    <div class="text-center">
                      <v-progress-circular
                        :size="130"
                        :width="15"
                        color="primary"
                        indeterminate
                      >채점중</v-progress-circular>
                    </div>
                  </v-img>             
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large">이미지를 업로드해주세요.</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              disabled
            >
              다음
            </v-btn>
          </div>
        </v-stepper-content>
        <v-stepper-content step="3" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">테스트 결과(1/1)</div>
          <v-card
            class="mb-12"
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
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">정수리능력시험 성적통지표</v-col>
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
                      :src="imageUrl" 
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
                      <v-col class="resultText" style="background-color: lightgray;">{{ nickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">구분</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">정수리 영역</v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">점수</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ result }} 점</v-col>
                </v-row>
                <v-row style="margin: auto;">
                  <v-col cols="3" class="resultBorder">등급</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ grade }} 등급</v-col>
                </v-row>
              </v-card>
              <v-row>
                <v-col class="pb-0 pt-5" style="font-family: 'Jua', sans-serif; font-size: large;">{{ this.nowDate }}</v-col>
              </v-row>
              <v-row class="mb-5">
                <v-col class="pt-0" style="font-family: 'Jua', sans-serif; font-size: large;">정수리영역평가원장</v-col>
              </v-row>
              <v-row v-if="grade < 4" class="gradeResult1 text-left" style="margin: auto;">                
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">3등급 이하</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">아직 안전한 단계</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large; color: white">두피를 청결하게 유지</span>
                  <span style="font-size: large;">하고 좋은 생활 습관을 통해 탈모를 예방하세요.</span>
                </v-col>
              </v-row>
              <v-row v-else-if="grade < 7" class="gradeResult2 text-left" style="margin: auto;"> 
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
              <v-row v-else-if="grade < 10" class="gradeResult3 text-left" style="margin: auto;">
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
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'test',
  components: {
  },
  data() {
      return {
        e1: 1,
        count: this.$route.params.count,
        files: [],
        imageUrl: '',
        selected: false,
        result: 100,
        searched: false,
        score: 0,
        uploadId: null,
        nowDate: null,
        nickname: null,
        grade: 1,
        isloading: false,
      }
  },
  created() {
    let today = new Date();
    let year = today.getFullYear()
    let month = today.getMonth() + 1
    let date = today.getDate()

    this.nowDate = `${year}.${month}.${date}`
    const token = sessionStorage.getItem('token')
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/api/accounts/user/`, 
      {
        headers: {Authorization: `token ${token}`}
      }
    )
    .then((re) => {
      this.user_id = re.data.id
      this.nickname = re.data.nickname
    })
    .catch(() => {})
  },
  methods: {
    reset() {
      this.selected = false
      this.imageUrl = ''
      this.searched = false
      this.uploadId = null
    },

    upload() {
      this.isloading = true
      this.searched = true
      this.e1 = 2
      this.score = parseInt(((210-(this.count * (this.count +1)) / 2)) * (5/21))
      let fd = new FormData();
      fd.append('files', this.files)
      let token = sessionStorage.getItem('token')
      axios.post('/api/api/images/analyze-image/',
        fd, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `token ${token}`,
          }
        }
      ).
      then((res) => {
        console.log('upload res', res)
        this.result = parseInt((100-res.data.result)/2) + this.score
        this.searched = true
        this.isloading = false
        this.e1 = 3
        this.uploadId = res.data.image.id
        console.log(this.el)
        if (this.result == 100) {
          this.grade = 1
        } else {
          this.grade = 10 - parseInt(this.result / 10)
        }
        this.saveResult()
      })
      .catch(() => {
        this.e1 = 1
        // console.log(this.el)
        alert('파일명이 한글입니다. 영어로 변경해 주세요.')
      });
    },
    saveResult() {
      let token = sessionStorage.getItem('token')
      axios.post('/api/api/images/save-score/', {'image': this.uploadId, 'score': this.result}, {
        headers: {
          'Authorization': `token ${token}`,
        }
      })
        .then((res) => {
          console.log('saveResult', res)
        })
    },
    onClickImageUpload() {
      this.selected = true
      this.$refs.imageInput.click()
    },
    onChangeImages(e) {
      this.files = e.target.files[0]
      this.imageUrl = URL.createObjectURL(this.files)
    },
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