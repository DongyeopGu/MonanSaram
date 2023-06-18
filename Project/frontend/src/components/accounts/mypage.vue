<template>
    <v-card 
    class="d-flex flex-column justify-space-around"
    height="100%"
    :loading="loading">
        <template slot="progress">
        <v-progress-linear
          :color="themeColor"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>
        <v-card-title>
        <span class="headline font-weight-bold blue--text text--darken-4">My Page</span>
        </v-card-title>
        <v-card-text>
        <v-container>
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
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="username">사용자 이름</label>
                    <v-text-field outlined readonly v-model="username" color="blue" id="username"></v-text-field>
                </v-col>
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="email">이메일 : </label>
                    <v-text-field outlined readonly v-model="email" color="blue" id="email"></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="nickname">닉네임</label>
                    <v-text-field outlined v-model="newNickname" color="blue" id="nickname"></v-text-field>
                </v-col>
                <v-col class="my-auto" cols=6>
                    <v-btn
                    :color="themeColor"
                    dark
                    @click="updateUsername"
                    >
                        닉네임 변경
                    </v-btn>
                </v-col>
                <!-- <v-col cols=6>
                    <label class="font-weight-bold teal--text" for="newPassword">새 비밀번호 : </label>
                    <v-text-field v-model="newPassword" color="teal" id="newPassword"></v-text-field>
                </v-col> -->
                <v-col cols=6>

                </v-col>
            </v-row>
            <v-row>
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="newpassword">변경할 비밀번호</label>
                    <v-text-field outlined v-model="newPassword" type="password" color="blue" id="newpassword"></v-text-field>
                </v-col>
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="checkpassword">비밀번호 확인</label>
                    <v-text-field outlined v-model="checkPassword" type="password" color="blue" id="checkpassword"></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols=6>
                    <label class="font-weight-bold blue--text text--darken-4" for="password">현재 비밀번호</label>
                    <v-text-field outlined v-model="password" type="password" color="blue" id="password"></v-text-field>
                </v-col>
                <v-col class="my-auto" cols=6>
                    <v-btn
                    :color="themeColor"
                    dark
                    @click="changePassword"
                >
                    비밀번호 수정
                </v-btn>
                </v-col>
            </v-row>
        </v-container>
        </v-card-text>
        <v-card-actions id="cardAction" class="align-center">
        <v-spacer></v-spacer>
        <v-btn
            :color="themeColor"
            dark
            @click="deleteUser"
        >
            회원탈퇴
        </v-btn>
        <v-btn
            :color="themeColor"
            dark
            @click="moveToBack"
        >
            뒤로가기
        </v-btn>
        
        </v-card-actions>
    </v-card>
</template>

<script>
import { mapMutations } from 'vuex';
import { getUserInfo, updateUsernameInfo, deleteUserInfo, updatePassword } from '@/api/index';
import { isEmpty, checkLogin } from '@/utils/index';

export default {
    name : 'mypage',
    data() {
        return {
            alert : false,
            themeColor : process.env.VUE_APP_THEME_COLOR,
            errorMessage : '',
            id : '',
            articles : null,
            email : '',
            compose : null,
            images : null,
            nickname : '',
            password : '',
            newNickname : '',
            newPassword : '',
            checkPassword : '',
            username : '',
            // newPassword : '',
            loading : false,
        }
    },
    computed : {

    },
    methods : {
        ...mapMutations([ 'setLogout' ]),

        showWarning(text) {
          this.errorMessage = text;
          this.alert = true;
          setTimeout(() => {
              this.alert = false;
          }, 1500);
          
        },

        async changePassword() {
            if (isEmpty(this.password)) {
                this.showWarning('현재 비밀번호를 입력해주세요.');
                return;
            } else if (isEmpty(this.newPassword)) {
                this.showWarning('변경할 비밀번호를 입력해주세요.');
                return;
            } else if (isEmpty(this.newPassword)) {
                this.showWarning('비밀번호를 확인해주세요.');
                return;
            } else {
                const userData = {
                username : this.username,
                password : this.password,
                newpassword : this.newPassword,
                checkpassword : this.checkPassword,
            };

            const response = await updatePassword(userData, sessionStorage.getItem('token'));

            const data = response.data;
            
            if (data.error) {
                this.showWarning(data.error);
                return;
            } else {
                alert('비밀번호 변경에 성공했습니다.');
                this.password = '';
                this.newPassword = '';
                this.checkPassword = '';
                return;
            }
            }
        },

        async updateUsername() {
            if (isEmpty(this.newNickname)) {
                this.showWarning('닉네임 칸을 작성해주세요.');
                return;
            } else if (this.nickname === this.newNickname) {
                this.showWarning('이미 이 닉네임을 사용하고 있습니다.');
                return;
            }

            const userData = {
                nickname : this.newNickname,
                username : this.username
            };
            const response = await updateUsernameInfo(userData, sessionStorage.getItem('token'));
            if (response.status === 200) {
                alert('회원정보가 정상적으로 수정되었습니다.')
            } else {
                alert('회원정보 수정에 실패하였습니다.')
                //console.log(response);
            }
        },
        async deleteUser() {
            const deleteUserCheck = confirm('정말로 탈퇴하시겠습니까?');
            if (deleteUserCheck) {
                const response = await deleteUserInfo(sessionStorage.getItem('token'));

                if (response.status === 200) {
                    alert('성공적으로 탈퇴하였습니다.');
                    this.$store.commit('setLogout');
                } else {
                    alert('회원탈퇴 과정에서 오류가 발생했습니다.')
                    //console.log(response);
                }
            } else {
                alert('회원탈퇴를 취소하셨습니다.');
            }
        },
        async updateUserPassword() {
            const userData = {
                username : this.username,
                newpassword : this.newPassword,
                checkpassword : this.checkPassword,
            };

            await updatePassword(userData, sessionStorage.getItem('token'));
            // console.log(response);
        },
        moveToBack() {
          this.$router.go(-1);
      },
      reserve () {
      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
      }

    },
    async created() {
        if (checkLogin()) {
            const response = await getUserInfo(sessionStorage.getItem('token'));
            const data = response.data;
            // console.log(data);
            this.id = data.id;
            this.articles = data.articles;
            this.compose = data.compose;
            this.email = data.email;
            this.images = data.images;
            this.nickname = data.nickname;
            this.username = data.username;
            this.newNickname = this.nickname;
        } else {
            alert('해당 기능을 이용하려면 로그인을 해야합니다.');
            this.$router.push({ name : 'login' });
        }
    },
    mounted() {

    },
}
</script>

<style scoped>

</style>