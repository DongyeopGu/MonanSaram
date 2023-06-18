<template>
  <v-container>
    <v-row><v-col class="text-center pb-0" style="font-family: 'Nanum Pen Script', cursive;"><h1>현재 나의 정수리 점수가</h1></v-col></v-row>
    <v-row><v-col class="text-center pt-0" style="font-family: 'Nanum Pen Script', cursive;"><h1>궁금하세요?</h1></v-col></v-row>

    <v-row>
      <v-col offset="1" class="text-center">
        <v-row>
          <v-col>
            <v-avatar
              color="primary"
              size="36"
            >
              <span class="white--text headline">1</span>
            </v-avatar>
          </v-col>
        </v-row>
      </v-col>
      <hr class="v-divider theme--light" style="margin: 40px auto !important;">
      <v-col class="text-center">
        <v-row>
          <v-col>
            <v-avatar
              color="primary"
              size="36"
            >
              <span class="white--text headline">2</span>
            </v-avatar>
          </v-col>
        </v-row>
      </v-col>
      <hr class="v-divider theme--light" style="margin: 40px auto !important;">
      <v-col class="text-center">
        <v-row>
          <v-col>
            <v-avatar
              color="primary"
              size="36"
            >
              <span class="white--text headline">3</span>
            </v-avatar>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
    <v-row class="text-center">
      <v-col class="pt-0 ml-2" style="font-family: 'Black Han Sans', sans-serif;">설문조사</v-col>
      <v-col class="pt-0" style="font-family: 'Black Han Sans', sans-serif;">AI 카메라</v-col>
      <v-col class="pt-0 mr-2" style="font-family: 'Black Han Sans', sans-serif;">테스트 결과</v-col>
    </v-row>
    <v-row 
      align="center"
      justify="center"
      style="height: 400px"
    > 
      <v-col class="d-flex flex-column justify-space-between align-center">
          <v-img
            src="../../assets/flower.png"
            width="300px"
          >
          </v-img>
        <div style="text-align : center;">
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="text-center">
        <router-link to="/survey" class="text-decoration-none" style="color: white; height: 56px; margin: 2px auto;">
          <v-chip
            class="ma-2"
            color="primary"
            large
            style="font-family: 'Do Hyeon', sans-serif; width: 240px; justify-content: center; font-size: medium"
          >
            탈모 테스트 시작하기 >
          </v-chip>
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

export default {
  data () {
    return {
    }
  },
  methods: {
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Nanum+Pen+Script&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');
</style>