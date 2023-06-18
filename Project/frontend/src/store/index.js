import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username : '',
    token : '',
  },
  getters : {
    getUsername(state) {
      return state.username;
    },
    getToken(state) {
      return state.token;
    },
  },
  mutations: {
    setLogin(state, payload) {
      state.username = payload.username;
      state.token = payload.token;
      sessionStorage.setItem('username', state.username);
      sessionStorage.setItem('token', state.token);
      //console.log(router.currentRoute.query.redirect);

      const path = (router.currentRoute.query.redirect == null)
						?	'/'
						: router.currentRoute.query.redirect
      router.push(path)
    },
    setLogout(state) {
      state.username = null;
      state.token = null;
      sessionStorage.clear();
      alert('로그아웃이 완료되었습니다. 홈 화면으로 이동합니다.')
      if (router.currentRoute.path === '/') {
        router.go(0)
      } else {
        router.push('/');
      }
    }
  },
  actions: {

  },
  modules: {
  }
})
