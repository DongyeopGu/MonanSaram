<template>
  <v-container>
    <v-row><v-col class="pl-4 pb-0"><h1 style="font-family: 'Hi Melody', cursive;">게시글 수정</h1></v-col></v-row>
    <v-btn
      color="#E3F2FD"
      depressed
      fab
      small
      absolute
      top
      right
      style="margin-top: 56px;"
      router :to="{ name: 'Community'}"
    >
      <v-icon>mdi-close-circle-outline</v-icon>
    </v-btn>
    <v-row>
      <v-col class="pt-0">
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        > 
          <v-row>
            <v-col cols="4" class="pl-4">
              <v-select
                v-model="category"
                :items="item"
                name='category'
                :rules="[v => !!v || '필수']"
                label="태그"
                required
                class="tagSelect"
                style="font-family: 'Jua', sans-serif;"
              ></v-select>
            </v-col>
            <v-col cols="8" class="pr-4">
              <v-text-field
                v-model="title"
                :counter="14"
                :rules="titleRules"
                name='title'
                label="제목"
                required
                style="font-family: 'Jua', sans-serif;"
              ></v-text-field>
            </v-col>
            <v-col class="px-4 pb-0">
              <v-textarea
                v-model="content"
                color="blue darken-3"
                name='content'
                :rules="[v => !!v || '필수']"
                outlined
                rows="10"
                clearable
                required
                clear-icon="mdi-close-circle"
                hide-details
                auto-grow
                style="font-family: 'Jua', sans-serif;"
              >
                <template v-slot:label>
                  <div>
                    내용
                  </div>
                </template>
              </v-textarea>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="pr-5 pb-0">
              <v-file-input
                chips
                v-model="uploadImages"
                name="files"
                multiple
                label="File input"
              ></v-file-input>
            </v-col>
          </v-row>
          
          <v-row>
            <v-col align="start" class="px-4">
              <span style="font-family: 'Hi Melody', cursive;">업로드 이미지</span><br>
              <div v-for="(file, index) in files" :key="file.id" class="py-3"
                  style="
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                font-family: 'Jua', sans-serif;
                font-size: small;
                max-width: 100%;
                height: 44px;"
                >
                <v-btn
                  @click="deleteFile(file)"
                  class="mx-2"
                  fab
                  height="20px"
                  width="20px"
                  color="dark"
                  depressed
                >
                  <v-icon dark>
                    mdi-minus
                  </v-icon>
                </v-btn>
                <span>{{ index + 1 }}. {{file.image.substring(38, file.image.length)}}</span>
                <br>
              </div>
              <hr class="mt-1">
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4" align="end">
              <v-btn
                :disabled="!valid"
                color="blue darken-3"
                @click="validate"
                dark
                small
              >
                <!-- <v-icon dark>
                  mdi-pencil
                </v-icon> -->
                <span style="font-family: 'Hi Melody', cursive; font-size: large">수정하기</span> 
              </v-btn>
              
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {

      article_id: this.$route.params.id,
      valid: true,
      title: '',
      content: '',
      titleRules: [
        v => !!v || '필수',
        v => (v && v.length <= 14) || '14자 이하만 가능합니다.',
      ],
      category: null,
      item: [
        '질문',
        '고민',
        '추천',
        '의견',
      ],
      checkbox: false,
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
      files: [],
      delFiles: [],
      uploadImages: null,
      fileID: [],
    }
  },
  methods: {
    async validate () {
      // this.$refs.form.validate()
      
      if (this.category == '고민') {
        this.items.category = '고민'
      } else if (this.category == '질문') {
        this.items.category = '질문'
      } else if (this.category == '추천') {
        this.items.category = '추천'
      } else if (this.category == '의견') {
        this.items.category = '의견'
      }
      const articleUpdateInfo = new FormData()

      articleUpdateInfo.append('category', this.items.category)
      articleUpdateInfo.append('title', this.title)
      articleUpdateInfo.append('content', this.content)
      articleUpdateInfo.append('user', this.items.user)
      if (this.uploadImages===null) {
        articleUpdateInfo.append('files', [])
        //console.log(this.uploadImages);
      } else {
        for (let i = 0; i < this.uploadImages.length; i++) {
          articleUpdateInfo.append('files', this.uploadImages[i]);
          //console.log(this.uploadImages);
        }
      }

      const token = sessionStorage.getItem("token")
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `token ${token}`
          }
      }
      let info = {'id':this.fileID}
      await axios.post(`${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/image-delete/`, info,
        {headers: {Authorization: `token ${token}`}})
        .then(()=>{
          // //console.log(res);
        })

      await axios.put(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/`, 
        articleUpdateInfo, config)
      .then((res) => {        
        this.$router.push({ name: "DetailArticle", params: { id: res.data.content.id } })
      })
      .catch(() => {alert('작성자가 아닙니다.')})
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
    deleteFile(file) {
      for(let i = 0; i < this.files.length; i++) {
        if (this.files[i]===file) {
          this.files.splice(i,1)
        }
      }
      this.fileID.push(file.id)
      // //console.log(this.fileID);
    },
  },
  created() {
    const token = sessionStorage.getItem("token")
    // //console.log(`/api/articles/article/${this.article_id}/`)
    axios.get(
      `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/${this.article_id}/`, 
      {headers: {Authorization: `token ${token}`}}
    )
    .then((res) => {
      // //console.log(res.data.images)
      this.items = res.data.detail
      this.files = res.data.images
      // res.data.images.forEach(e => {
      //   this.files.push(e.image)
      //   this.fileID.push(e.id)
      // });

      // 카테고리
      if (res.data.detail.category == 1) {
        this.category = '고민'
      } else if (res.data.detail.category == 2) {
        this.category = '질문'
      } else if (res.data.detail.category == 3) {
        this.category = '추천'
      } else if (res.data.detail.category == 4) {
        this.category = '의견'
      }
      this.title = res.data.detail.title
      this.content = res.data.detail.content
    })
    .catch(() => {})
  }
}
</script>

<style>

</style>