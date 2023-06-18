<template>
  <v-container>
    <v-row><v-col><v-btn @click="clickCreatArticle()">글쓰기</v-btn></v-col></v-row>
    
  <div>
    <v-data-table
      :items="items"
      item-key="aritlcie_id"
      class="elevation-1"
      :search="search"
      :custom-filter="filterOnlyCapsText"
      hide-default-header
    >
      <template v-slot:top>
        <v-text-field
          v-model="search"
          label="검색"
          class="mx-4"
        ></v-text-field>
      </template>
      <template v-slot:header>
        <thead>
          <tr>
            <!-- <th class="tagCol pr-0">태그</th> -->
            <th class="titleCol text-center pr-0 pl-2">제목</th>
            <th class="userCol text-right pr-0 pl-1">글쓴이</th>
            <th class="timeCol text-right pr-0 pl-1">작성일</th>
            <th class="viewCol text-right pr-0 pl-1">조회</th>
            <th class="recommendCol text-right pr-2 pl-1">추천</th>
          </tr>
        </thead>
      </template>
      <template v-slot:body="{ items }">
        <tbody>
          <tr v-for="item in items" :key="item.article_id" @click="clickArticle(item.article_id)">
            <!-- <td class="tagCol pr-0">{{ item.tag }}</td> -->
            <td class="titleCol pr-0 pl-2">[{{ item.tag }}] {{ item.title }}</td>
            <td class="userCol text-right pr-0 pl-1">{{ item.user }}</td>
            <td class="timeCol text-right pr-0 pl-1">{{ item.time }}</td>
            <td class="viewCol text-right pr-0 pl-1">{{ item.view }}</td>
            <td class="recommendCol text-right pr-2 pl-1">{{ item.recommend }}</td>
          </tr>
        </tbody>
      </template>
    </v-data-table>
  </div>

  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      search: '',
      items: [],
      tagCategroy: null,
      upload: null,
      page: 1,
      totalPage: 1,
      pageItems: [],
      isLoggedIn: false,
    }
  },
  created() {
    // API로 커뮤니티 전체글 GET
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/api/articles/`)
    .then((res) => {
      //console.log('community 전체글', res.data)
      let tempTotalPage = res.data.articles.length
      this.totalPage = parseInt(tempTotalPage / 10)
      if (tempTotalPage % 10 > 0) {
        this.totalPage += 1
      }
      for (let i=0; i < res.data.articles.length; i++){
        // 카테고리
        if (res.data.articles[i].category == 1) {
          this.tagCategory = '고민'
        } else if (res.data.articles[i].category == 2) {
          this.tagCategory = '질문'
        } else if (res.data.articles[i].category == 3) {
          this.tagCategory = '추천'
        } else if (res.data.articles[i].category == 4) {
          this.tagCategory = '의견'
        }
        // 날짜
        const month = res.data.articles[i].upload_date.substring(5,7)
        const day = res.data.articles[i].upload_date.substring(8,10)
        this.upload = month + '.' + day // +'.' + res.data.articles[i].upload_date.substring(11,16)

        this.items.push({
          tag: this.tagCategory,
          title: res.data.articles[i].title,
          user: res.data.articles[i].nickname,
          recommend: res.data.articles[i].recommendation_users.length,
          time: this.upload,
          view: res.data.articles[i].hits,
          article_id: res.data.articles[i].id
        })
      }
      this.items.reverse()
      this.pageItems = this.items.slice(0, 10)
      // console.log(this.pageItems)
      // console.log(this.items)
    })
    .catch(() => {})
    sessionStorage.getItem('username') && sessionStorage.getItem('token') ? this.isLoggedIn = true : this.isLoggedIn = false;
    //console.log('로그인유무', !!this.isLoggedIn)
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
    pageChange(value) {
      this.page = value
      this.pageItems = this.items.slice((value-1)*10, (value-1)*10+10)
    },

    ////
    
    filterOnlyCapsText (value, search) {
      return value != null &&
        search != null &&
        typeof value === 'string' &&
        value.toString().toLocaleUpperCase().indexOf(search) !== -1
    },
  },
  
}
</script>

<style>
.communityForm tr td {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  /* max-width: 140px; */
}

.tagCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.titleCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 120px;
  max-width: 120px;
}

.userCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.timeCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 27px;
  max-width: 27px;
}

.viewCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 25px;
  max-width: 25px;
}

.recommendCol {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 25px;
  max-width: 25px;
}
</style>