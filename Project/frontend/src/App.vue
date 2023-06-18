<template>
  <v-app id="inspire" style="min-width: 320px">
    <div>
      <v-app-bar
      :color="themeColor"
      dark
      fixed
      >
        <v-app-bar-nav-icon @click="clickIcon()"></v-app-bar-nav-icon>

        <v-toolbar-title class="font-weight-bold px-0">
          <router-link 
            to='/' 
            class="px-0 mx-0 text-decoration-none" 
            style="color: white; font-family: 'Hi Melody', cursive; font-size: x-large;">
            모난사람
          </router-link>
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-list-item-group>
          <v-list-item v-for="icon in topIconList" :key="icon.index" :class="topIconClass">
            <v-tooltip v-model="icon.tooltipShow" :color="tooltipColor" top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon :class="iconClass" @click="icon.func">{{ icon.icon }}</v-icon>
                </v-btn>
              </template>
              <span>{{ icon.tooltip }}</span>
            </v-tooltip>
          </v-list-item>
        </v-list-item-group>
      </v-app-bar>
  
      <v-navigation-drawer
        v-model="drawer"
        absolute
        temporary
        clipped
      >
        <v-list
          nav
          dense
        >
          <v-list-item-group
            v-model="group"
            :active-class="themeBtnColor"
          >
            <router-link to='/' class="mx-auto my-auto text-decoration-none">
              <v-list-item>
                <v-list-item-icon>
                  <v-icon>{{'mdi-home'}}</v-icon>
                </v-list-item-icon>
                <v-list-item-title style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  메인
                </v-list-item-title>
              </v-list-item>
            </router-link>
            <router-link to='/mypage' class="mx-auto my-auto text-decoration-none">
              <v-list-item>
                <v-list-item-icon>
                  <v-icon>{{'mdi-account'}}</v-icon>
                </v-list-item-icon>
                <v-list-item-title style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  프로필
                </v-list-item-title>
              </v-list-item>
            </router-link>
            <router-link to='/community' class="mx-auto my-auto text-decoration-none">
              <v-list-item>
                <v-list-item-icon>
                  <v-icon>{{'mdi-account-group'}}</v-icon>
                </v-list-item-icon>
                <v-list-item-title style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  게시판
                </v-list-item-title>
              </v-list-item>
            </router-link>
            <v-list-item>
                <v-list-item-icon>
                  <v-icon>{{'mdi-power-standby'}}</v-icon>
                </v-list-item-icon>
                <v-list-item-title v-if="isLoggedin" @click="logout" style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  로그아웃
                </v-list-item-title>
                <v-list-item-title v-else @click="moveToLogin" style="font-family: 'Nanum Pen Script', cursive; font-size: x-large">
                  로그인
                </v-list-item-title>
              </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>  
    </div>
    <div style="height: 56px;"></div>
    <v-main>
      <router-view/>
    </v-main>    

    <template>
      <v-footer
        padless
        fixed
        sytle="height: 56px; !important"
      >
        <v-card
          flat
          tile
          class="blue darken-4 text-center"
          style="width: 100%;"
        >
          <v-card-text 
            class="pt-0 pb-0"
            style="height: 56px;"
          >
            <v-row 
              justify="center"
              no-gutters
              style="height: 56px;"
            >
              <v-bottom-navigation
                absolute
                background-color="blue darken-4" 
                dark
                color="white"
              > 
                <v-col class="pt-2 pr-1 pl-1">
                  <v-btn class="pr-1 pl-1" @click="scrollTop()">
                    <router-link to="/" class="text-decoration-none mr-0 ml-0" style="color: white; height: 56px; margin: 2px auto;">
                      <v-icon class="mx-auto my-auto">{{'mdi-home'}}</v-icon>
                      <br><span style="font-family: 'Noto Sans KR', sans-serif;">홈</span>
                    </router-link>
                  </v-btn>
                </v-col>

                <v-col class="pt-2 pr-1 pl-1">
                  <v-btn class="pr-1 pl-1" @click="scrollTop()">
                    <router-link to="/survey_init" class="text-decoration-none mr-0 ml-0" style="color: white; height: 56px; margin: 2px auto;">
                      <v-icon class="mx-auto my-auto">{{'mdi-checkbox-marked-outline'}}</v-icon>
                      <br><span style="font-family: 'Noto Sans KR', sans-serif;">테스트</span>
                    </router-link>
                  </v-btn>
                </v-col>

                <v-col class="pt-2 pr-1 pl-1">
                  <v-btn class="pr-1 pl-1" @click="scrollTop()">
                    <router-link to="/funnyImage_init" class="text-decoration-none mr-0 ml-0" style="color: white; height: 56px; margin: 2px auto;">
                      <v-icon class="mx-auto my-auto">{{'mdi-camera'}}</v-icon>
                      <br><span style="font-family: 'Noto Sans KR', sans-serif;">합성</span>
                    </router-link>
                  </v-btn>
                </v-col>

                <v-col class="pt-2 pr-1 pl-1">
                  <v-btn class="pr-1 pl-1" @click="scrollTop()">
                    <router-link to="/community" class="text-decoration-none mr-0 ml-0" style="color: white; height: 56px; margin: 2px auto;">
                      <v-icon class="mx-auto my-auto">{{'mdi-account-group'}}</v-icon>
                      <br><span style="font-family: 'Noto Sans KR', sans-serif;">게시판</span>
                    </router-link>
                  </v-btn>
                </v-col>
              </v-bottom-navigation>
            </v-row>
          </v-card-text>
        </v-card>
      </v-footer>
    </template>
    <div style="height: 56px;"></div>
  </v-app>  
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'App',

  data() {
    let moveToLogin = this.moveToLogin;
    let moveToMypage = this.moveToMypage;
    let logout = this.logout;

    return {
      themeColor : null,
      themeBtnColor : null,
      topIconClass : 'd-inline m-auto',
      topIconList : null,
      tooltipColor : null,
      iconClass : '',
      mainListClass : 'my-auto',
      footerTabClass : 'mx-auto text-button',
      footerTabText : '',
      isLoggedin: false,
      navList : [
          {name : 'Home', icon : 'mdi-home', index : 0},
          {name : 'My Page', icon : 'mdi-account', index : 1},
          {name : 'Test', icon : 'mdi-camera', index : 2},
          {name : 'Community', icon : 'mdi-account-group', index : 3},
          {name : 'Survey', icon : 'mdi-checkbox-marked-outline', index : 4},
      ],
      loginIconList : [
          {name : 'My Page', icon : 'mdi-account', index : 0, func : moveToMypage, tooltip : '마이 페이지', tooltipShow : false},
          {name : 'Logout', icon : 'mdi-logout', index : 1, func : logout, tooltip : '로그아웃', tooltipShow : false},
      ],
      logoutIconList : [
          {name : 'Sign In', icon : 'mdi-power-standby', index : 0, func : moveToLogin, tooltip : '로그인', tooltipShow : false},
      ],
      tabList : [
          {name : 'Main', index : 0},
          {name : 'AI', index : 1},
          {name : 'Daily', index : 2},
          {name : 'Community', index : 3},
      ],
      drawer : false,
      group : null,
    }
  },

  components: {

  },

  methods : {
    ...mapMutations([ 'setLogout' ]),

    moveToLogin() {
        if (this.$route.name !== 'login') {
          this.$router.push({ name : 'login' });
        }    
      },
    moveToMypage() {
      if (this.$route.name !== 'mypage') {
        this.$router.push({ name : 'mypage' });
      }    
    },
    logout() {
      if (sessionStorage.getItem('username') && sessionStorage.getItem('token')) {
        this.$store.commit('setLogout');
      }
    },
    moveToNavList(index) {
      if (index == 0) {
        //console.log('home')
        this.$router.push({ name: 'index' })
      } else if (index == 1) {
        //console.log('my page')
      } else if (index == 2) {
        //console.log('test')
      } else if (index == 3) {
        // //console.log('community')
        this.$router.push({ name: 'Community' })
      } else if (index == 4) {
        // //console.log('survey')
        this.$router.push('/survey')
      }
    },
    
    clickIcon() {
      this.$vuetify.goTo(0)
      this.drawer = true
    },

    scrollTop() {
      this.$vuetify.goTo(0)
    }
  },

  created() {
    this.themeColor = process.env.VUE_APP_THEME_COLOR
    this.themeBtnColor = process.env.VUE_APP_THEME_BUTTON_COLOR
    this.tooltipColor = process.env.VUE_APP_THEME_TOOLTIP_COLOR
    sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.topIconList = this.loginIconList : this.topIconList = this.logoutIconList
    sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.isLoggedin = true : this.isLoggedin = false
  },
  
  updated() {
    sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.topIconList = this.loginIconList : this.topIconList = this.logoutIconList
        sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.isLoggedin = true : this.isLoggedin = false
  },

};
</script>

<style >
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gugi&display=swap');


</style>