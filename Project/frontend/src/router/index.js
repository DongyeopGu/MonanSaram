import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '@/components/index'
import error from '@/components/error'
import login from '@/components/accounts/login'
// 설문조사
import Survey from '@/views/Survey/Survey.vue'
import SurveyResult from '@/views/Survey/SurveyResult.vue'
// 커뮤니티
import Community from '@/views/Community/Community.vue'
import CreateArticle from '@/views/Community/CreateArticle.vue'
import DetailArticle from '@/views/Community/DetailArticle.vue'
import UpdateArticle from '@/views/Community/UpdateArticle.vue'
import test from '@/views/Analyze/test.vue'
import FunnyImage from '@/views/Analyze/FunnyImage.vue'
import InitSurvey from '@/views/Survey/InitSurvey.vue'
import FunnyImageInit from '@/views/Analyze/FunnyImageInit.vue'

Vue.use(VueRouter)

const routes = [
  {
    path : '/',
    name : 'index',
    component : index
  },
  {
    path : '/login',
    name : 'login',
    component : login
  },
  {
    path : '/signup',
    name : 'signup',
    component : () => import('@/components/accounts/signup')
  },
  {
    path : '/mypage',
    name : 'mypage',
    component : () => import('@/components/accounts/mypage')
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/community'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/community/create',
    name: 'CreateArticle',
    component: CreateArticle,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/community/create'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/community/:id',
    name: 'DetailArticle',
    component: DetailArticle,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/community/:id'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/community/update/:id',
    name: 'UpdateArticle',
    component: UpdateArticle,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/community/update/:id'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/survey',
    name: 'Survey',
    component: Survey,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({path: '/login', query: {redirect: '/survey'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/survey/result',
    name: 'SurveyResult',
    component: SurveyResult
  },
  {
    path: '/test',
    name: 'test',
    component: test,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/test'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/compose',
    name: 'FunnyImage',
    component: FunnyImage,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({name: 'login', query: {redirect: '/compose'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/survey_init',
    name: 'InitSurvey',
    component: InitSurvey,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({path: '/login', query: {redirect: '/survey'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path: '/funnyImage_init',
    name: 'FunnyImageInit',
    component: FunnyImageInit,
    beforeEnter(to, from, next) {
      if (sessionStorage.getItem('token')!=null) {
        next()
      } else {
        let confirms = confirm('로그인이 필요한 페이지입니다. 로그인 페이지로 이동하시겠습니까?')
        if (confirms) {
          next({path: '/login', query: {redirect: '/survey'}})
        } else {
          next('/')
        }
      }
    }
  },
  {
    path : '/*',
    name : '404',
    component : error
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
