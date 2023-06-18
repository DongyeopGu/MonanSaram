<template>
  <v-container class="px-5">
    <v-row v-if="!flagOfResult"><v-col class="text-center pb-0 pt-0" style="font-family: 'Nanum Pen Script', cursive;"><h1>원하는 사진으로</h1></v-col></v-row>
    <v-row v-if="!flagOfResult"><v-col class="text-center pt-0" style="font-family: 'Nanum Pen Script', cursive;"><h1>합성해드려요!</h1></v-col></v-row>
    <!-- 카로우셀 -->
    <v-carousel v-model="model" v-if="!flagOfResult" hide-delimiters>
      <v-carousel-item
        v-for="(images, i) in testImage"
        :key="i"
      >
        <v-sheet
          tile
          color="grey lighten-4"
        >
          <v-row>
            <v-col offset="1" cols="5">
              <v-card>
                <v-img 
                  :src="`/api/api/default/`+images[0]" 
                  height="200" 
                  width="100%"
                  cover
                  @click="pickImage(images[0])"
                ></v-img>
              </v-card>
            </v-col>
            <v-col cols="5">
              <v-card>
                <v-img 
                  :src="`/api/api/default/`+images[1]" 
                  height="200" 
                  width="100%"
                  cover
                  @click="pickImage(images[1])"
                ></v-img>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col offset="1" cols="5" class="">
              <v-card>
                <v-img 
                  :src="`/api/api/default/`+images[2]" 
                  height="200" 
                  width="100%"
                  cover
                  @click="pickImage(images[2])"
                ></v-img>
              </v-card>
            </v-col>
            <v-col cols="5">
              <v-card>
                <v-img 
                  :src="`/api/api/default/`+images[3]" 
                  height="200"
                  width="100%"
                  cover
                  @click="pickImage(images[3])"
                ></v-img>
              </v-card>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="text-center pt-1"><span style="font-family: 'Nanum Pen Script', cursive; color: black; font-size: xx-large;">사진을</span></v-col>
            <v-col class="text-center pt-1"><span style="font-family: 'Nanum Pen Script', cursive; color: black; font-size: xx-large;">고르세요</span></v-col>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-row
      v-if="!searched"
      id="#upload-image"
    > 
      <!-- 선택할 이미지 -->
      <v-col cols="6">
        <v-card 
          v-if="imageUrl2"
          @click="onClickImageUpload2"
        >
          <v-img 
            :src="`/api/api/default/`+pickedImage" 
            v-if="!baseImageUrl"
            height="250" 
            width="100%" 
            cover
          ></v-img>
          <v-img v-else :src="baseImageUrl" width="100%" height="250" cover></v-img>
          <input ref="imageInput2" type="file" hidden @change="onChangeImages2">
        </v-card>
        <v-card 
          v-else
          width="100%" 
          height="250"
          color="grey lighten-2" 
          class="d-flex justify-center align-center grey--text" 
          @click="onClickImageUpload2"
        >
          <v-img v-if="baseImageUrl" :src="baseImageUrl" width="100%" height="250" cover></v-img>
          <input ref="imageInput2" type="file" hidden @change="onChangeImages2">
          <span v-if="!baseImageUrl" style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: xx-large">선택한 이미지</span>
        </v-card>
      </v-col>
      <!-- 업로드 이미지 -->
      <v-col cols="6">
        <v-card 
          v-if="imageUrl"
          @click="onClickImageUpload" 
        >
          <v-img :src="imageUrl" width="100%" height="250" cover></v-img>
          <input ref="imageInput" type="file" hidden @change="onChangeImages">
        </v-card>
        <v-card 
          v-if="!imageUrl"
          @click="onClickImageUpload" 
          width="100%" 
          height="250"  
          color="grey lighten-2" 
          class="justify-center align-center grey--text"
        >
          <input  ref="imageInput" type="file" hidden @change="onChangeImages">
          <v-row
            no-gutters
            style="height: 100px;"
          >
            <v-col align-self="end" class="text-center">
              <span style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: xx-large">클릭해서</span>
            </v-col>
          </v-row>
          <v-row
            no-gutters
            style="height: 50px;"
          >
            <v-col align-self="center" class="text-center">
              <span style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: xx-large">합성할 이미지를</span>
            </v-col>
          </v-row>
          <v-row
            no-gutters
            style="height: 100px;"
          >
            <v-col align-self="start" class="text-center">
              <span style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: xx-large">업로드하세요</span>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <!-- 버튼 -->
    <v-row v-if="!searched">
      <v-col cols="12" justify="center" align="center">
        <v-btn 
          @click='upload' 
          color="blue darken-3"
          dark 
          class="button-word2 font-weight-bold"
        >합성하기</v-btn>
      </v-col>
    </v-row>

    <!-- 합성 중 바 -->
    <v-row 
      v-else-if="isloading" 
      align="center" 
      justify="center" 
      class="mx-auto my-auto" 
    >
      <v-col 
        cols="12" 
        class="text-center"
        style="color: #1565C0; font-family: 'Single Day', cursive; font-weight: bold; font-size: xx-large"
      >합성 중입니다</v-col>
      <v-col cols="12" class="px-0">
        <v-progress-linear color="grey" indeterminate rounded height="6"></v-progress-linear>
      </v-col>
    </v-row>
    <!-- 결과 및 게시판 공유 -->
    <v-row v-else>
      <v-row id="result-image">
        <v-col class="text-center pb-0 pt-0" style="font-family: 'Nanum Pen Script', cursive;">
          <h1>합성 사진</h1>
        </v-col>
      </v-row>
      <v-col cols="12" justify="center" align="center">
        <v-card>
          <v-img 
            id="compose-image"
            :src="'/api'+result"  
            alt="compose-image" 
            width="100%"
            height="400"
            cover
          ></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" justify="center" align="center">
        <v-btn 
          @click="goBack" 
          class="button-word2 font-weight-bold"
          style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: large"
        >뒤로 가기</v-btn>
      </v-col>
      <v-col cols="12">
        <v-divider></v-divider>
      </v-col>
      <v-row>
        <v-col class="text-center pb-0 pt-0" style="font-family: 'Nanum Pen Script', cursive;">
          <h1>게시글에 공유해보세요!</h1>
        </v-col>
      </v-row>
      <v-col cols="12" class="pb-2 pt-0">
        <v-text-field
          label="제목"
          v-model="title"
          :rules="rules"
          :counter="14"
          style="font-family: 'Noto Sans KR', sans-serif;"
        ></v-text-field>
      </v-col>
      <v-col cols="12" class="pt-1">
        <v-textarea 
          v-model="content" 
          :value="content"
          label="내용"
          outlined
          hide-details
          auto-grow
          rows="3"
          style="font-family: 'Noto Sans KR', sans-serif;"
        ></v-textarea>
      </v-col>
      <v-col cols="12" class="text-right pb-1 pt-0">
        <v-btn 
          @click="ch" 
          color="blue darken-3" 
          dark
          style="font-family: 'Nanum Pen Script', cursive; font-weight: bold; font-size: large"
        >게시글 공유</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'test',
  created() {
    const token = sessionStorage.getItem('token')
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/api/accounts/user/`, 
      {
        headers: {Authorization: `token ${token}`}
      }
    )
    .then((re) => {
      this.nickname = re.data.nickname
    })
    .catch(() => {})
  },
  data() {
    return {
      model: 0,
      nickname: '',
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length <= 14) || '14자 이하',
      ],
      files: [],
      imageUrl: '',
      selected: false,
      result: null,
      flagOfResult: false,
      searched: false,
      isloading: false,
      score: 0,
      check: null,
      composefile: null,
      Url: '',
      articleInfo: new FormData(),
      title: '재미로 보는 탈모사진',
      content: '',
      testImage: [
        ['blue.jpg', 'blue_long.jpg', 'gullit.jpg', 'joker.jpg'], 
        ['juhomin.jpg', 'kimkyungho.jpg', 'kimsangho.jpg', 'zidane.jpg'],
        ['Ahn_Ji-young.PNG', 'Captain_America.PNG', 'Dwayne_Johnson.PNG', 'Ezreal.PNG'],
        ['green.PNG', 'Harley_Quinn.PNG', 'Huh_Jae.PNG', 'Jungwoo_Ha.PNG'],
        ['KimJeungEun.PNG', 'Ma_Dongseok.PNG', 'V.PNG', 'Yun_A.PNG']
      ],
      defaultImage: ['blue.jpg', 'blue_long.jpg', 'gullit.jpg', 'joker.jpg', 'juhomin.jpg', 'kimkyungho.jpg', 'kimsangho.jpg', 'zidane.jpg'],

      // 
      pickedImage: '',
      imageUrl2: '',
      baseImageUrl: '',
      selected2: false,
      files2: [],

    }
  },
  methods: {
    reset() {
      this.selected = false
      this.imageUrl = ''
      this.imageUrl2 = ''
      this.searched = false
      this.isloading = false
      this.selected2 = false
      this.baseImageUrl = ''
    },
    upload() {
      if (!this.imageUrl2 && !this.baseImageUrl) {
        alert('이미지를 선택해주세요')
        return false
      } else if (!this.imageUrl) {
        alert('이미지를 업로드 해주세요')
        return false
      } 
      this.isloading = true
      this.searched = true
      let fd = new FormData();
      fd.append('path', this.pickedImage)
      fd.append('base', this.files2)
      fd.append('files', this.files)
      let token = sessionStorage.getItem('token')
      axios.post('/api/api/images/compose-image/',
        fd, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `token ${token}`,
          }
        }
      ).then((res) => {
        this.result = res.data.result
        this.isloading = false
        this.Url = '/api'+this.result
        this.flagOfResult = true
        this.content = `${ this.pickedImage.slice(0, -4) } ${ this.nickname } 합성 사진입니다. `
        this.moveToResult()
      })
      .catch(() => {
        // console.log('얼굴 못찾는 error', err)
        this.reset()
        alert('파일 이름에 한글이 들어가 있거나 얼굴을 찾지 못하였습니다.')
      });
    },
    onClickImageUpload() {
      this.selected = true
      this.$refs.imageInput.click()
    },
    onChangeImages(e) {
      this.files = e.target.files[0]
      let nameLength = e.target.files[0].name.length
      let verifyFile = e.target.files[0].name.slice(nameLength-3, nameLength) 
      if (verifyFile == 'PNG' || verifyFile == 'jpg' || verifyFile == 'png' || verifyFile == 'JPG') {
        this.imageUrl = URL.createObjectURL(this.files)
      } else {
        alert('jpg 또는 PNG 파일형식만 가능합니다.')
        return false
      }
    },
    goBack() {
      this.flagOfResult = false
      this.reset()
    },
    async ch() {
      // console.log(this.composefile);
      // let articleInfo = new FormData()
      await this.append()

      const token = sessionStorage.getItem("token")
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `token ${token}`
          }
      }      
      await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/`, 
        this.articleInfo, config)
      .then((res) => {
        this.$router.push({ name: "DetailArticle", params: { id: res.data.content.id } })
        // console.log(res);
      })
      .catch(()=> {})
    },
    async appendFile() {
      const res = await fetch(this.Url)
      const blob = await res.blob()
      let now = Date.now()
      let file = new File([blob], `if_i_am_bald${now}.jpg`, blob)
      return file
    },
    async append() {
      this.composefile = await this.appendFile()
      this.articleInfo.append('category', '의견')
      this.articleInfo.append('title', this.title)
      this.articleInfo.append('content', this.content)
      this.articleInfo.append('files', this.composefile)
    },
    pickImage(img) {
      this.pickedImage = img
      this.imageUrl2 = `/api/api/default/${img}`
      this.moveToUpload()
      this.baseImageUrl = ''
      this.files2 = []
    },
    moveToUpload() {
      document.getElementById('#upload-image').scrollIntoView()
    },
    moveToResult() {
      this.$nextTick(function () {
        this.$vuetify.goTo(0)
      })
    },
    onClickImageUpload2() {
      this.selected2 = true
      this.$refs.imageInput2.click()
    },
    onChangeImages2(e) {

      this.files2 = e.target.files[0]
      let nameLength = e.target.files[0].name.length
      let verifyFile = e.target.files[0].name.slice(nameLength-3, nameLength) 
      if (verifyFile == 'PNG' || verifyFile == 'jpg' || verifyFile == 'png' || verifyFile == 'JPG') {
        this.baseImageUrl = URL.createObjectURL(this.files2)
      } else {
        alert('jpg 또는 PNG 파일형식만 가능합니다.')
        return false
      }
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Single+Day&display=swap');
.v-input--is-label-active {
  padding-left: 10px;
}

.v-input__slot {
  margin-bottom: 5px;
}
</style>