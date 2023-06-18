<template>
  <v-container>
    <div id="face" style="height: 1000px">
      <div id="textPosition">
        <v-row class="pt-12"><v-col class="text-center pb-0" style="font-family: 'Nanum Pen Script', cursive; font-size: x-large"><h1>재미로 보는</h1></v-col></v-row>
        <v-row><v-col class="text-center pt-0" style="font-family: 'Nanum Pen Script', cursive;  font-size: x-large"><h1>FACE 체인지</h1></v-col></v-row>
      </div>
      <div id="btnPosition">
        <v-row>
          <v-col class="text-center">
            <router-link to="/compose" class="text-decoration-none" style="color: white; height: 56px; margin: 2px auto;">
              <v-chip
                class="ma-2"
                color="primary"
                large
                dark
                style="font-family: 'Do Hyeon', sans-serif; width: 240px; justify-content: center; font-size: large"
              >
                합성 시작하기 >
              </v-chip>
            </router-link>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="text-center">
            <v-chip
              class="ma-2"
              color="blue darken-2"
              large
              dark
              outlined
              @click="moveToDescription"
              style="font-family: 'Do Hyeon', sans-serif; width: 240px; justify-content: center; font-size: large"
            >
              설명 보러가기 >
            </v-chip>
          </v-col>
        </v-row>
      </div>
    </div>

    <v-row
      id="description-image">
      <v-col>
        <v-card
          color="blue darken-3"
          dark
        >
          <v-card-title class="title py-2">
            <span style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">1. 원하는 이미지를 선택하세요!</span>
          </v-card-title>
          <v-card-text class="white text--primary">
            <v-row 
              align="center"
              justify="center"
            > 
              <v-col class="d-flex flex-column justify-space-between align-center">
                  <v-img
                    src="../../assets/1.gif"
                  >
                  </v-img>
                <div style="text-align : center;">
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card
          color="blue darken-3"
          dark
        >
          <v-card-title class="title py-2">
            <span style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">2. 합성할 이미지를 업로드하세요</span>
          </v-card-title>
          <v-card-text class="white text--primary">
            <v-row 
              align="center"
              justify="center"
            > 
              <v-col class="d-flex flex-column justify-space-between align-center">
                  <v-img
                    src="../../assets/2.gif"
                  >
                  </v-img>
                <div style="text-align : center;">
                </div>
              </v-col>
            </v-row>
            <v-row 
              align="center"
              justify="center"
            > 
              <v-col class="d-flex flex-column justify-space-between align-center">
                <span style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  hint) 원하는 이미지가 없다면 선택한 이미지를 클릭하여 원하는 이미지를 업로드하세요!
                </span>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card
          color="blue darken-3"
          dark
        >
          <v-card-title class="title py-2">
            <span style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">3. 합성하고 게시글로 공유해봐요~</span>
          </v-card-title>
          <v-card-text class="white text--primary">
            <v-row 
              align="center"
              justify="center"
            > 
              <v-col class="d-flex flex-column justify-space-between align-center">
                  <v-img
                    src="../../assets/3.gif"
                  >
                  </v-img>
                <div style="text-align : center;">
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    
    <v-row>
      <v-col>
        <v-row>
          <v-col class="text-center">
            <div class="text-decoration-none" style="color: white; height: 56px; margin: 2px auto;">
              <v-chip
                class="ma-2"
                color="primary"
                large
                style="font-family: 'Do Hyeon', sans-serif; width: 240px; justify-content: center; font-size: large"
                @click="scrollTop()"
              >
                합성 하러가기 >
              </v-chip>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>


  </v-container>
</template>

<script>
export default {
  data () {
    return {
      descriptionFlag: false,
      innerHeight: window.innerHeight - 100,
    }
  },
  mounted() {
    // document.getElementById('face').style.height = this.innerHeight + "px"
    document.getElementById('face').style.height = this.innerHeight + "px"
    // console.log(document.getElementById('face'))
  },
  methods: {
    moveToDescription() {
      this.descriptionFlag = true
      document.getElementById('face').style.height = this.innerHeight + "px"
      this.$nextTick(function () {
        this.moveToScroll()
      })
    },
    moveToScroll() {
      this.$nextTick(function () {
        this.$vuetify.goTo(document.getElementById('description-image'), { offset: 56 })
      })
    },
    scrollTop() {
      this.$vuetify.goTo(0)
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Pen+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

#btnPosition {
  position: relative;
  top: 20%;
}

#textPosition { 
  position: relative;
  top: 5%;
}
</style>