<template>
  <v-container>
    <v-row><v-col class="pl-4 pb-0"><h1 style="font-family: 'Hi Melody', cursive;">게시글 작성</h1></v-col></v-row>
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
                outlined
                rows="10"
                clearable
                required
                clear-icon="mdi-close-circle"
                hide-details
                :rules="[v => !!v || '필수']"
                auto-grow
                style="font-family: 'Jua', sans-serif; "
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
                v-model="files"
                name="files"
                multiple
                label="File input"
              ></v-file-input>
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
                <span style="font-family: 'Hi Melody', cursive; font-size: large">작성하기</span> 
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
      files: null,
      
    }
  },
  methods: {
    async validate() {
      // this.$refs.form.validate()
      let articleInfo = new FormData()
      articleInfo.append('category', this.category)
      articleInfo.append('title', this.title)
      articleInfo.append('content', this.content)
      if (this.files===null) {
        articleInfo.append('files', [])
      } else {
        for (let i = 0; i < this.files.length; i++) {
          articleInfo.append('files', this.files[i]);
        }
      }

      const token = sessionStorage.getItem("token")
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `token ${token}`
          }
      }
      await axios.post(
        `${process.env.VUE_APP_BACKEND_URL}/api/articles/article/`, 
        articleInfo, config)
      .then((res) => {
        this.$router.push({ name: "DetailArticle", params: { id: res.data.content.id } })
      })
      .catch(()=> {})
    },
    reset () {
      this.$refs.form.reset()
    },
    resetValidation () {
      this.$refs.form.resetValidation()
    },
  },
}
</script>

<style>
.tagSelect {
  /* white-space: nowrap;  */
  min-width: 65px;
}

label {
  font-family: 'Hi Melody', cursive;
}

</style>