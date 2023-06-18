<template>
  <v-container style="height: 100%">
    <v-card
      class="d-flex flex-column justify-space-around"
      height="100%"
      :loading="loading"
    >
      <template slot="progress">
        <v-progress-linear
          :color="themeColor"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>
      <v-card-title
      
      >
        <span
          class="font-weight-bold blue--text text--darken-4"
          style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: xx-large;"
          >로그인</span
        >
      </v-card-title>
      <v-card-text
      
      >
        <v-row>
          <v-alert
            v-model="alert"
            transition="slide-y-transition"
            dense
            outlined
            type="error"
          >
            {{ errorMessage }}
          </v-alert>
        </v-row>
        <v-row>
          <v-col offset="1" cols="10">
            <v-text-field
              label="아이디*"
              outlined
              v-model="username"
              :color="themeColor"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1" cols="10">
            <v-text-field
              label="비밀번호*"
              outlined
              v-model="password"
              :color="themeColor"
              type="password"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
            <v-col align="end">
                
                <v-btn :color="themeColor" text @click="login" style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: large;">
                로그인
                </v-btn>
            </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions id="cardAction" class="align-center">
        <v-spacer></v-spacer>
        <findpassword />
        <v-btn class="pr-5" :color="themeColor" text @click="moveToSignup" style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: large;">
          회원가입
        </v-btn>

        <!-- <v-btn>
              <v-img src="@/static/login/kakao_login_medium_narrow.png" />
          </v-btn> -->
      </v-card-actions>
    </v-card> 
  </v-container>
</template>

<script>
import findpassword from '@/components/accounts/findpassword';
import { mapMutations } from 'vuex';
import { loginUser } from '@/api/index';
import { isEmpty, checkLogin } from '@/utils/index';

export default {
    name : 'login',
    data() {
        return {
            alert : false,
            themeColor : process.env.VUE_APP_THEME_COLOR,
            errorMessage : '',
            username : '',
            password : '',
            loading : false,
            kakaoWidth : null,
            kakaoHeight : null,
        }
    },
    computed : {
    
    },
    methods : {
        ...mapMutations([ 'setLogin' ]),

        showWarning(text) {
          this.errorMessage = text;
          this.alert = true;
          setTimeout(() => {
              this.alert = false;
          }, 1500);
          
      },
      async login() {
          if (isEmpty(this.username)) {
              this.showWarning('아이디를 입력해주세요.');
              return;
          } else if (isEmpty(this.password)) {
              this.showWarning('비밀번호를 입력해주세요.');
              return;
          }
          const userData = {
              username : this.username,
              password : this.password
          };
          const response = await loginUser(userData);

          if (response.data.error) {
              const err = response.data.error;
              let message = '';
              if (err.username) {
                  message = err.username;
              } else if (err.password) {
                  message = err.password
              }
              this.showWarning(message);
          } else {
              this.$store.commit('setLogin', {username : response.data.user.username, token : response.data.token});
          }

      },

      moveToSignup() {
          this.$router.push({ name : 'signup' });
      },

      reserve () {
      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
      },
    },
    // created() {
    //     sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.$router.push({ name : 'index' }) : null;
    // },
    components : {
        findpassword
    },
    created() {
        checkLogin() ? this.$router.push({ name : 'index' }) : null;
    },
    mounted() {
        // let cardAction = document.getElementById('cardAction');
        // this.kakaoWidth = cardAction.offsetWidth/10;
        // this.kakaoHeight = cardAction.offsetHeight/2;
        // //console.log(this.kakaoWidth, this.kakaoHeight);
    },
}
</script>

<style scoped>

</style>
