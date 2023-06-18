<template>
    <v-dialog
      v-model="dialog"
      persistent
      max-width="290"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="blue darken-4"
          text
          v-bind="attrs"
          v-on="on"
          style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: large;"
        >
          비밀번호 찾기
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="font-weight-bold blue--text text--darken-4"
        style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: x-large;"
        >
          비밀번호 찾기
        </v-card-title>
        <v-card-text class="pb-0">
            <v-container class="pb-0">
                <v-row>
                    <v-col cols=12>
                  <label class="font-weight-bold blue--text text--darken-4" for="username">사용자 이름</label>
                  <v-text-field outlined v-model="username" color="blue" id="username"></v-text-field>
              </v-col>
              <v-col cols=12>
                  <label class="font-weight-bold blue--text text--darken-4" for="email">이메일</label>
                  <v-text-field outlined v-model="email" color="blue" id="email"></v-text-field>
              </v-col>
                </v-row>
            </v-container>
        </v-card-text>
        <v-card-actions class="pb-4 pr-5">
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-4"
            dark
            @click="dialog = false"
            style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: large;"
          >
            취소
          </v-btn>
          <v-btn
            color="blue darken-4"
            dark
            @click="sendEmail"
            style="color: white; font-family: 'Do Hyeon', sans-serif; font-size: large;"
          >
            비밀번호 찾기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import { findPassword } from '@/api/index';
import { isEmpty } from '@/utils/index';

export default {
    name : 'findpassword',
    data() {
        return {
            dialog : false,
            username : '',
            email : '',
        }
    },
    props : {
    },
    methods : {
      async sendEmail() {
        if(isEmpty(this.username)) {
          alert('사용자 이름을 입력해주세요.');
          return ;
        } else if (isEmpty(this.email)) {
          alert('이메일을 입력해주세요.');
          return;
        } else {
          const userData = {
          username : this.username,
          email : this.email,          
          };

          const response = await findPassword(userData);

          const apiMessage = response.data.message;

          alert(apiMessage);

          this.dialog = false;
          return;  
        }   
      }
    },
    computed : {

    },
    created() {

    },
}
</script>

<style>

</style>