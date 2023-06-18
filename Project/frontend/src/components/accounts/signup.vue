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
      <v-card-title>
        <span 
          class="font-weight-bold blue--text text--darken-4"
          style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: xx-large;"
        >회원가입</span
        >
      </v-card-title>
      <v-card-text>
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
            <v-col>
              <v-text-field
                label="아이디*"
                outlined
                :color="themeColor"
                v-model="username"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <v-text-field
                label="비밀번호*"
                outlined
                :color="themeColor"
                type="password"
                v-model="password"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                label="비밀번호 확인*"
                outlined
                :color="themeColor"
                type="password"
                v-model="passwordCheck"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <v-text-field
                label="닉네임*"
                outlined
                :color="themeColor"
                v-model="nickname"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                label="이메일*"
                outlined
                :color="themeColor"
                v-model="email"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        <small class="red--text" style="font-family: 'Do Hyeon', sans-serif; font-size: medium;">*표시는 반드시 작성해야 합니다.</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          :color="themeColor"
          text
          @click="moveToBack"
          style="font-family: 'Do Hyeon', sans-serif; font-size: large;"
        >
          뒤로가기
        </v-btn>
        <v-btn
          :color="themeColor"
          text
          @click="signUp"
          style="font-family: 'Do Hyeon', sans-serif; font-size: large;"
        >
          회원가입
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { mapMutations } from "vuex";
import { registerUser } from "@/api/index";
import { isEmpty, checkLogin, checkEmail, checkPassword } from "@/utils/index";

export default {
  name: "signup",
  data() {
    return {
      alert: false,
      themeColor: process.env.VUE_APP_THEME_COLOR,
      errorMessage: "",
      username: "",
      nickname: "",
      email: "",
      password: "",
      passwordCheck: "",
      loading: false,
      ages: ["20대 미만", "20대", "30대", "40대", "50대", "60대 이상"],
      interests: ["탈모 진단", "두피 상식", "두피 관리 정보"],
    };
  },
  computed: {},
  methods: {
    ...mapMutations(["setLogin"]),

    moveToBack() {
      this.$router.go(-1);
    },
    showWarning(text) {
      this.errorMessage = text;
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
      }, 1500);
    },
    async signUp() {
      if (isEmpty(this.username)) {
        this.showWarning("아이디를 입력해주세요.");
        return;
      } else if (isEmpty(this.password)) {
        this.showWarning("비밀번호를 입력해주세요.");
        return;
      } else if (isEmpty(this.email)) {
        this.showWarning("이메일을 입력해주세요.");
        return;
      } else if (!checkEmail(this.email)) {
        this.showWarning("이메일 양식을 맞춰서 작성해야합니다.");
        return;
      } else if (this.password && isEmpty(this.passwordCheck)) {
        this.showWarning("비밀번호를 확인해주세요.");
        return;
      } else if (!checkPassword(this.password, this.passwordCheck)) {
        this.showWarning("비밀번호가 다릅니다.");
        return;
      }

      const userData = {
        username: this.username,
        nickname: this.nickname,
        email: this.email,
        password: this.password,
      };

      const response = await registerUser(userData);

      // console.log(response);

      if (response.data.error) {
        const err = response.data.error;
        let message = "";
        if (err.username) {
          message = err.username;
        } else if (err.password) {
          message = err.password;
        }
        this.showWarning(message);
      } else {
        this.$store.commit("setLogin", {
          username: response.data.user.username,
          token: response.data.token,
        });
      }
    },
    reserve() {
      this.loading = true;

      setTimeout(() => (this.loading = false), 2000);
    },
  },
  created() {
    checkLogin() ? this.$router.push({ name: "index" }) : null;
  },
};
</script>

<style scoped></style>
