<template>
  <v-container class="pt-0">
    <v-btn
      id="btnArticleCreate"
      class="mx-2"
      fab
      dark
      large
      color="cyan"
      @click="clickCreatArticle()"
    >
      <v-icon dark>
        mdi-pencil
      </v-icon>
    </v-btn>

    <v-row class="mb-5">
      <v-tabs
        background-color="blue darken-4"
        dark
        v-model="tab"
        fixed-tabs
        flat
        show-arrows
        center-active
      >
        <v-tab @click="clickTab(0)" style="font-family: 'Hi Melody', cursive; font-size: medium;">전체{{ tabOneLength }}</v-tab>
        <v-tab @click="clickTab(1)" style="font-family: 'Hi Melody', cursive; font-size: medium;">고민{{ tabTwoLength }}</v-tab>
        <v-tab @click="clickTab(2)" style="font-family: 'Hi Melody', cursive; font-size: medium;">질문{{ tabThreeLength }}</v-tab>
        <v-tab @click="clickTab(3)" style="font-family: 'Hi Melody', cursive; font-size: medium;">추천{{ tabFourLength }}</v-tab>
        <v-tab @click="clickTab(4)" style="font-family: 'Hi Melody', cursive; font-size: medium;">의견{{ tabFiveLength }}</v-tab>
      </v-tabs>
    </v-row>
    <v-tabs-items 
      v-model="tab"
    > 
      <div v-for="item in pageItems" :key="item.article_id">
        <v-row>
          <v-img
            v-if="item.image != ''"
            :src="'/api'+item.image"
            height="80px"
            width="80px"
            max-height="80px"
            max-width="80px"
            @click="clickArticle(item.article_id)"
          ></v-img>
          <v-col class="pt-0 pb-0">
            <v-row>
              <v-col v-if="item.numberOfComment === 0" class="titleStyle pb-2 pt-2" @click="clickArticle(item.article_id)">{{ item.title }}</v-col>
              <v-col v-else class="titleStyle pb-2 pt-2" @click="clickArticle(item.article_id)">{{ item.title }}</v-col>
              <p v-if="item.image != ''" class="titleStyle pb-2 pt-2 mb-0" @click="clickArticle(item.article_id)">({{ item.numberOfComment }})</p>
              <p v-else class="titleStyle pb-2 pt-2 mb-0 pl-2" @click="clickArticle(item.article_id)">({{ item.numberOfComment }})</p>
            </v-row>
            <v-row class="mb-0">
              <v-col class="tagStyle" v-if="item.tag === '추천'"><p class="mb-4" style="cursor:pointer; border-left: 5px solid Coral; padding-left: 10px;">{{ item.tag }}</p></v-col>
              <v-col class="tagStyle" v-if="item.tag === '의견'"><p class="mb-4" style="cursor:pointer; border-left: 5px solid DeepPink; padding-left: 10px;">{{ item.tag }}</p></v-col>
              <v-col class="tagStyle" v-if="item.tag === '고민'"><p class="mb-4" style="cursor:pointer; border-left: 5px solid BlueViolet; padding-left: 10px;">{{ item.tag }}</p></v-col>
              <v-col class="tagStyle" v-if="item.tag === '질문'"><p class="mb-4" style="cursor:pointer; border-left: 5px solid Chartreuse; padding-left: 10px;">{{ item.tag }}</p></v-col>
              <v-col class="viewStyle">조회 {{ item.view }}</v-col>
              <v-col class="recommendStyle">추천 {{ item.recommend }}</v-col>
              <v-col class="timeStyle">{{ item.time }}</v-col>
            </v-row>
          </v-col>
        </v-row>
        <hr style="border-top: 1px solid #D3D3D3; border-bottom: 0px;">
      </div>

      <!-- 페이지네이션 -->
      <v-pagination
        v-model="page"
        :length="totalPage"
        :total-visible="5"
        @input="pageChange(page, fullItems[tab])"
        class="mt-5"
        light
      >
      </v-pagination>
    </v-tabs-items>
    
  </v-container>
</template>

<script>
import axios from 'axios';
import {
  mdiPencil,
} from '@mdi/js'

// window.onload = function()
// {
//   this.$vuetify.goTo(0)
// }
export default {
  data () {
    return {
      icons: {
        mdiPencil,
      },
      search: '',
      items: [],
      tagCategroy: null,
      upload: null,
      numberOfComment: 0,
      page: 1,
      totalPage: 1,
      pageItems: [],
      tagOne: [],
      tagTwo: [],
      tagThree: [],
      tagFour: [],
      fullItems: [],
      isLoggedIn: false,
      tab: 0,
      tabOneLength: 0,
      tabTwoLength: 0,
      tabThreeLength: 0,
      tabFourLength: 0,
      tabFiveLength: 0,
    }
  },
  mounted() {
    
    this.$vuetify.goTo(0)
  },
  created() {
    // API로 커뮤니티 전체글 GET
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/api/articles/`)
    .then((res) => {
      //console.log('community 전체글', res.data)
      let tempTotalPage = res.data.articles.length
      this.totalPage = parseInt(tempTotalPage / 7)
      if (tempTotalPage % 7 > 0) {
        this.totalPage += 1
      }
      for (let i=0; i < res.data.articles.length; i++){
        // 날짜
        const year = res.data.articles[i].upload_date.substring(0,4)
        const month = res.data.articles[i].upload_date.substring(5,7)
        const day = res.data.articles[i].upload_date.substring(8,10)
        this.upload = year + '.' + month + '.' + day // +'.' + res.data.articles[i].upload_date.substring(11,16)

        // 카테고리
        if (res.data.articles[i].category == 1) {
          this.tagCategory = '고민'
          if (res.data.articles[i].image != "") {
            this.tagOne.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: res.data.articles[i].image[0].image
            })
          } else {
            this.tagOne.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: ""
            })
          }
        } else if (res.data.articles[i].category == 2) {
          this.tagCategory = '질문'
          if (res.data.articles[i].image != "") {
            this.tagTwo.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: res.data.articles[i].image[0].image
            })
          } else {
            this.tagTwo.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: ""
            })
          }
        } else if (res.data.articles[i].category == 3) {
          this.tagCategory = '추천'
          if (res.data.articles[i].image != "") {
            this.tagThree.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: res.data.articles[i].image[0].image
            })
          } else {
            this.tagThree.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: ""
            })
          }
        } else if (res.data.articles[i].category == 4) {
          this.tagCategory = '의견'
          if (res.data.articles[i].image != "") {
            this.tagFour.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: res.data.articles[i].image[0].image
            })
          } else {
            this.tagFour.push({
              tag: this.tagCategory,
              title: res.data.articles[i].title,
              user: res.data.articles[i].nickname,
              recommend: res.data.articles[i].recommendation_users.length,
              time: this.upload,
              view: res.data.articles[i].hits,
              article_id: res.data.articles[i].id,
              numberOfComment: res.data.articles[i].comment.length,
              image: ""
            })
          }
        }

        
        if (res.data.articles[i].image != "") {
          this.items.push({
            tag: this.tagCategory,
            title: res.data.articles[i].title,
            user: res.data.articles[i].nickname,
            recommend: res.data.articles[i].recommendation_users.length,
            time: this.upload,
            view: res.data.articles[i].hits,
            article_id: res.data.articles[i].id,
            numberOfComment: res.data.articles[i].comment.length,
            image: res.data.articles[i].image[0].image
          })
        } else {
          this.items.push({
            tag: this.tagCategory,
            title: res.data.articles[i].title,
            user: res.data.articles[i].nickname,
            recommend: res.data.articles[i].recommendation_users.length,
            time: this.upload,
            view: res.data.articles[i].hits,
            article_id: res.data.articles[i].id,
            numberOfComment: res.data.articles[i].comment.length,
            image: ""
          })
        }
      }
      // this.items.reverse()
      this.pageItems = this.items.slice(0, 7)
      this.fullItems.push(this.items, this.tagOne, this.tagTwo, this.tagThree, this.tagFour)
      this.tabOneLength = this.items.length
      this.tabTwoLength = this.tagOne.length
      this.tabThreeLength = this.tagTwo.length
      this.tabFourLength = this.tagThree.length
      this.tabFiveLength = this.tagFour.length
    })
    .catch(() => {})
    sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.isLoggedIn = true : this.isLoggedIn = false;
    // //console.log('로그인유무', !!this.isLoggedIn)
  },
  methods: {
    // 글쓰기 버튼 클릭
    clickCreatArticle() {
      if (!this.isLoggedIn) {
        alert('로그인이 필요합니다')
      } else {
        this.$router.push({ name: 'CreateArticle' })
      }
    },
    // 테이블에 게시글 클릭
    clickArticle(article_id) {
      if (!this.isLoggedIn) {
        alert('로그인이 필요합니다')
      } else {
        this.$router.push({ name: "DetailArticle", params: { id: article_id } })
      }

    },
    // 페이지네이션
    pageChange(value, tagPageItems) {
      // //console.log('page', value, tagPageItems)
      this.page = value
      // this.pageItems = this.items.slice((value-1)*10, (value-1)*10+10)
      this.pageItems = tagPageItems.slice((value-1)*7, (value-1)*7+7)
    },
    
    filterOnlyCapsText (value, search) {
      //console.log('aaa', value, search)
      return value != null &&
        search != null &&
        typeof value === 'string' &&
        value.toString().toLocaleUpperCase().indexOf(search) !== -1
    },
    clickTab(p) {
      this.page = 1
      let tempTotalPage = this.fullItems[p].length
      this.totalPage = parseInt(tempTotalPage / 7)
      if (tempTotalPage % 7 > 0) {
        this.totalPage += 1
      }
      //console.log(this.page, this.totalPage, p)
      this.pageItems = this.fullItems[p].slice(0, 7)
    }
  },
  
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@100;300&display=swap');

.titleStyle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-family: 'Jua', sans-serif;
  font-size: 20px;
  max-width: 90%;
  height: 44px;
}

.tagStyle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 70px;
  max-width: 70px;
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 18px;
  font-family: 'Noto Sans KR', sans-serif;
}

.viewStyle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 58px;
  max-width: 58px;
  padding-left: 0px;
  padding-right: 0px;
  color: #778899;
  padding-top: 4px;
  padding-bottom: 0px;
  font-family: 'Noto Sans KR', sans-serif;
}

.recommendStyle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 58px;
  max-width: 58px;
  padding-left: 0px;
  padding-right: 0px;
  color: #778899;
  padding-top: 4px;
  padding-bottom: 0px;
  font-family: 'Noto Sans KR', sans-serif;
}

.timeStyle {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 90px;
  max-width: 90px;
  padding-left: 0px;
  padding-right: 0px;
  color: #778899;
  padding-top: 4px;
  padding-bottom: 0px;
  font-family: 'Noto Sans KR', sans-serif;
}

#btnArticleCreate {
  position:fixed;
  right:0px;
  bottom:70px;
  z-index:1000;

}

.v-pagination__item {
  font-size: 14px !important;
  height: 20px !important;
  min-width: 20px !important;
  padding-right: 0px !important;
  padding-left: 0px !important;
}

.v-pagination__navigation {
  font-size: 20px !important;
  height: 20px !important;
  min-width: 20px !important;
  max-width: 20px !important;
}

</style>