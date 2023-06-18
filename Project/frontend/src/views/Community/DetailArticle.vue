<template>
  <v-container>
    <v-row>
      <v-col class="pb-0 pt-0">
        <span v-if="this.items.category == '질문'">🧐</span>
        <span v-if="this.items.category == '고민'">🤔</span>
        <span v-if="this.items.category == '추천'">🤗</span>
        <span v-if="this.items.category == '의견'">😁</span>
        <span style="font-family: 'Poor Story', cursive; font-size: x-large">{{ this.items.category }}</span>
        <span v-if="this.items.category == '질문'">🧐</span>
        <span v-if="this.items.category == '고민'">🤔</span>
        <span v-if="this.items.category == '추천'">🤗</span>
        <span v-if="this.items.category == '의견'">😁</span>
      </v-col>
      <v-col class="pb-0 pt-0" align="end">
        <v-btn
          small 
          router :to="{ name: 'Community'}"
          style="font-family: 'Do Hyeon', sans-serif;"
        >목록가기</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col 
        cols="9"
        class="detailTitle pb-0 pt-0 pr-0" 
        style="font-family: 'Do Hyeon', sans-serif;"
      >{{ this.items.title }}
      </v-col>
      <v-col cols="3" align-self="end" class="pb-0 pl-0 text-right">
        <span style="font-family: 'Gamja Flower', cursive;"> {{ this.items.upload_date }}</span> 
      </v-col>
    </v-row>
    <v-row>
      <v-col
        class="pt-0 detailInfo" 
        style="border-style: none none ridge none"
        cols="4"
      >
        <span class="mdi mdi-chess-king"></span>
        <span style="font-family: 'Jua', sans-serif; color: #311B92;">{{ this.items.nickname }}</span>
        
      </v-col>
      <v-col 
        class="detailInfo pt-0 text-right"
        style="border-style: none none ridge none"
      > 
        
        <span style="font-family: 'Gamja Flower', cursive;">
          조회{{ this.items.hits }} 추천{{ this.items.recommendation_users.length }} 댓글{{ this.comments.length }}
        </span> 
      </v-col>
    </v-row>
    <v-row>
      <v-col class="pb-0" style="word-break: break-all; font-family: 'Gothic A1', sans-serif; font-size: small">{{ this.items.content }}</v-col>
    </v-row>
    <v-row
      align="center"
      justify="center"
    >
      <v-col 
        cols="6"
        sm="4"
        md="3"
        class="pb-0" 
        align="center"
        v-for="img in items.image"
        :key="img.image"
      >
        <img
          :src="'/api'+img.image"
          width="100%"
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col align="end" style="border-style: none none ridge none">
        <v-btn class="mr-2" @click="clickUpdate(article_id)" small v-if="items.user == this.user_id" style="font-family: 'Do Hyeon', sans-serif;">
          수정
        </v-btn>
        <v-btn color="" small @click="deleteArticle" v-if="items.user == this.user_id" style="font-family: 'Do Hyeon', sans-serif;">
          삭제
        </v-btn>
      </v-col>
    </v-row>
    <!-- 댓글들 -->
    <v-row align="center">
      <v-col class="pt-2 pb-0 text-center">
        <span style="font-family: 'Gamja Flower', cursive; font-size: x-large">전체 댓글 {{ this.comments.length }}개</span>
      </v-col>
      <v-col class="text-center pt-2 pb-0">
        <v-icon @click="clickRecommend" color="" v-if="!this.liked">mdi-thumb-up-outline</v-icon>
        <v-icon @click="clickRecommend" color="blue" v-else>mdi-thumb-up</v-icon>
        <p class="mb-0" style="font-family: 'Gothic A1', sans-serif; font-size: small;">추천 {{ this.items.recommendation_users.length }}</p>
        <!-- <p v-else style="margin-bottom: 19px;"></p> -->
      </v-col>
    </v-row>

    <div v-for="(comment, index) in comments" :key="comment.id">
      <v-row align="center">
        <v-col class="commentNickname pl-4 py-0" style="font-family: 'Jua', sans-serif; color: #311B92;">
          {{ comment.nickname }}
        </v-col>
        <v-col class="text-right py-0">
          <v-btn v-if="comment.user == user_id" icon @click.stop="clickOption(comment.id, index)">
            <v-icon>mdi-dots-horizontal</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row style="border-bottom-style: solid; border-bottom-color: lightgray; border-bottom-width: thin">
        <v-col class="pt-0" style="white-space:pre-line; word-break: break-all; font-family: 'Gothic A1', sans-serif; font-size: small;">
          {{ comment.content }}
        </v-col>
      </v-row>
    </div>
    
    <v-navigation-drawer
      v-model="drawer"
      bottom
      temporary
      fixed
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item class="text-center">
            <v-list-item-title>
              <v-row>
                <v-col>
                  <v-btn 
                    @click="clickRecommentUpdate(recomment_id, recomment_index)"
                    block 
                    large
                  >
                    <span style="font-family: 'Gothic A1', sans-serif; font-size: x-large;">수정</span>
                  </v-btn> 
                </v-col>
              </v-row>
            </v-list-item-title>
          </v-list-item>
          <v-list-item class="text-center">
            <v-list-item-title>
              <v-row>
                <v-col>
                  <v-btn 
                    @click="clickRecommentDelete(recomment_id, recomment_index)"
                    block 
                    large
                  >
                    <span style="font-family: 'Gothic A1', sans-serif; font-size: x-large;">삭제</span>
                  </v-btn> 
                </v-col>
              </v-row>
            </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <!-- 댓글 작성 -->
    <v-row id="update-recomment">      
      <v-col>
        <v-textarea
          v-if="!flag"
          clearable
          clear-icon="mdi-close-circle"
          outlined
          label="댓글 작성"
          v-model="recomment"
          :value="recomment"
          hide-details
          auto-grow
          rows="3"
        ></v-textarea>
        <v-textarea
          v-if="flag"
          background-color="light-blue lighten-5"
          clearable
          clear-icon="mdi-close-circle"
          label="댓글 수정"
          v-model="recomment"
          :value="recomment"
          outlined
          hide-details
          auto-grow
          rows="3"
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row v-if="!flag">
      <v-col class="pt-0" align="end">
        <v-btn
          tile
          dark
          @click="clickRecomment(article_id)"
          small
          style="background-color: #1565C0;"
        >
          <v-icon left>
            mdi-pencil
          </v-icon>
          댓글 등록
        </v-btn>
      </v-col>
    </v-row>
    <!-- 댓글 수정 -->
    <v-row v-if="flag">
      <v-col align="end">
        <v-btn
          tile
          color="primary"
          small
          @click="clickRecommentBtn(update_comment_id, index)"
        >
          <v-icon left>
            mdi-pencil
          </v-icon>
          댓글 수정
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      drawer: false,
      group: null,
      article_id: this.$route.params.id,
      items: {
        category: null,
        content: null,
        hits: null,
        id: null,
        image: null,
        nickname: null,
        recommendation_users: [],
        title: null,
        update_date: null,
        upload_date: null,
        user: null,
        username: null,
      },
      recomment: '',
      comments: {},
      index: 0,
      flag: false,
      update_comment_id: null,
      liked: false,
      user_id: null,
      recomment_id: null,
      recomment_index: null,
    }
  },
  created() {
    const token = sessionStorage.getItem("token")
    // article 내용 가져오기
    axios.get(
      `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/`, 
      {headers: {Authorization: `token ${token}`}}
    )
    .then((res) => {
      this.items = res.data.detail
      this.items.image = res.data.images
      
      // 카테고리
      if (res.data.detail.category == 1) {
        this.items.category = '고민'
      } else if (res.data.detail.category == 2) {
        this.items.category = '질문'
      } else if (res.data.detail.category == 3) {
        this.items.category = '추천'
      } else if (res.data.detail.category == 4) {
        this.items.category = '의견'
      }

      const year = res.data.detail.upload_date.substring(0,4)
      const month = res.data.detail.upload_date.substring(5,7)
      const day = res.data.detail.upload_date.substring(8,10)
      this.items.upload_date = year + '.' + month + '.' + day


      this.comments = res.data.comments
      
      // 추천했는지 안했는지 판단
      axios.get(
        `${process.env.VUE_APP_BACKEND_URL}/api/accounts/user/`, 
        {headers: {Authorization: `token ${token}`}}
      )
      .then((re) => {
        this.user_id = re.data.id
        for (let i=0; i < this.items.recommendation_users.length; i++) {
          if (this.items.recommendation_users[i] == this.user_id) {
            this.liked = true
            break
          }
        }
      })
      .catch(() => {})
    })
    .catch(() => {})

  },
  methods: {
    async test() {
      const token = sessionStorage.getItem("token")
      await axios.get(
        `${process.env.VUE_APP_BACKEND_URL}/api/accounts/user/`, 
        {headers: {Authorization: `token ${token}`}}
      )
      .then((res) => {
        this.user_id = res.data.id
        for (let i=0; i < this.items.recommendation_users.length; i++) {
          if (this.items.recommendation_users[i] == this.user_id) {
            this.liked = true
            break
          }
        }
      })
      .catch(() => {})

    },

    // 게시글 수정 페이지 이동
    clickUpdate(article_id) {
      let confirmed = confirm('수정하시겠습니까?')
      if (confirmed) {
        this.$router.push({ name: "UpdateArticle", params: { id: article_id } })
      }
    },
    
    // 댓글 등록
    clickRecomment(article_id) {
      const token = sessionStorage.getItem("token")
      const commentInfo = {
        "content": this.recomment
      }
      axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/comment_create/`, 
        commentInfo,
        {headers: {Authorization: `token ${token}`}}
      )
      .then(() => {
        this.$router.go({ name: "DetailArticle", params: { id: article_id } })
        this.recomment = ''
      })
      .catch(() => {})
    },

    // 댓글 삭제
    clickRecommentDelete(comment_id) {
      this.drawer = !this.drawer
      const token = sessionStorage.getItem("token")
      axios.delete(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/${comment_id}/comment_update/`, 
        {headers: {Authorization: `token ${token}`}}
      )
      .then(() => {
        //console.log(res.data.message)
        this.$router.go({ name: "DetailArticle", params: { id: this.article_id } })
      })
      .catch(() => {})
    },

    // 댓글 수정
    clickRecommentUpdate(comment_id, index) {
      this.recomment = this.comments[index].content
      this.flag = true
      this.update_comment_id = this.comments[index].id
      this.drawer = !this.drawer
      this.moveToUpdate()
    },

    // 댓글 수정 버튼 클릭
    clickRecommentBtn(comment_id) {
      const token = sessionStorage.getItem("token")
      const commentInfo = {
        'content': this.recomment
      }
      axios.put(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/${comment_id}/comment_update/`, 
        commentInfo,
        {headers: {Authorization: `token ${token}`}}
      )
      .then(() => {
        this.$router.go({ name: "DetailArticle", params: { id: this.article_id } })
      })
      .catch(() => {})
    },

    // 게시글 삭제
    deleteArticle() {
      const token = sessionStorage.getItem("token")
      let confirmed = confirm('삭제하시겠습니까?')
      if (confirmed) {
          axios.delete(
          `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/`, 
          {headers: {Authorization: `token ${token}`}}
        )
        .then(() => {
          alert('삭제 완료되었습니다.')
          this.$router.push('/community')
        })
        .catch(() => {
          alert('작성자가 아닙니다.')
        })
      }
    },

    // 추천
    clickRecommend() {
      const token = sessionStorage.getItem("token")
      axios.get(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/recommendation/`, 
        {headers: {Authorization: `token ${token}`}}
      )
      .then((res) => {
        this.liked = res.data.liked
        if (this.liked) {
          this.items.recommendation_users.push(this.user_id)
        } else {
          this.items.recommendation_users.pop()
        }
      })
    },

    // 옵션 클릭
    clickOption(id, index) {
      this.drawer = !this.drawer
      this.recomment_id = id
      this.recomment_index = index
    },

    // 스크롤
    moveToUpdate() {
      document.getElementById('update-recomment').scrollIntoView()
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Gothic+A1:wght@600&family=Hi+Melody&family=Jua&family=Nanum+Pen+Script&family=Noto+Sans+KR:wght@300&family=Poor+Story&display=swap');

.detailTitle {
  font-size: x-large;
}

.detailInfo {
  font-size: medium;
}

.commentNickname {
  white-space: nowrap;
}

.commentContent {
  word-break: break-all;
}

.commentUpdate {
  white-space: nowrap;
  max-width: 50px;
}

.commentDelete {
  /* white-space: nowrap; */
  /* max-width: 500px; */
}

.headNickname {
  /* text-overflow: ellipsis; */
  /* min-width: 100px; */
  
}

.headContent {
  /* text-overflow: ellipsis; */
  /* min-width: 500px; */
}
</style>