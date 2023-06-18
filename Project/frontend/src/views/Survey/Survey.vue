<template>
  <v-container>
    <v-stepper v-model="e1" alt-labels class="d-flex flex-column justify-space-between align-center mt-1">
      <h3 v-if="this.e1 < 5" class="pt-2">쉿🤐..정수리 시험 중..!!</h3>
      <h3 v-else class="pt-2">정수리 시험 점수는..✨😲</h3>
      <v-stepper-items>
        <v-stepper-content step="1" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">설문조사 (1/3)</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            max-width="500px"
            min-width="300px"
          >
            <v-card-text class="pb-1">
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex1" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">가족</span><span class="surbeyNomal">(친가, 외가 조부모/부모, 형제) 중 머리숱이 적거나</span> 
                        <span class="surbeyHighlight"> 대머리</span><span class="surbeyNomal">가 있다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex2" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">보통 사람보다 가슴, 턱, 팔, 다리 등에 </span>
                        <span class="surbeyHighlight">체모가 많고 굵은 편</span><span class="surbeyNomal">이다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex3" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">두피</span><span class="surbeyNomal">가 말랑말랑하지 않고 </span><span class="surbeyHighlight">딱딱한 편</span>
                        <span class="surbeyNomal">이다. </span>
                        <span class="surbeyHighlight">체모가 많고 굵은 편</span><span class="surbeyNomal">이다. </span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex4" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">정수리</span><span class="surbeyNomal">가 종이같이 </span>
                        <span class="surbeyHighlight">팽팽하고 당겨지는 느낌</span><span class="surbeyNomal">이 있다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex5" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">두피</span><span class="surbeyNomal">가 따갑고 </span>
                        <span class="surbeyHighlight">예민</span><span class="surbeyNomal">하다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex6" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">머리가 자주 </span>
                        <span class="surbeyHighlight">가렵고, 비듬이 많다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex7" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">최근 </span>
                        <span class="surbeyHighlight">모발</span>
                        <span class="surbeyNomal">이 가늘어지고 </span>
                        <span class="surbeyHighlight">힘이 없다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row class="pb-0 text-right">
                <v-col class="pb-0 text-right" style="font-family: 'Noto Serif KR', serif; color: gray">출처: 대한탈모치료학회</v-col>
              </v-row>
            </v-card-text>
          </v-card>
          <div class="text-right">
            <v-btn
              color="primary"
              @click="e1 = 2"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>
        </v-stepper-content>
  
        <v-stepper-content step="2" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">설문조사 (2/3)</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
          >
            <v-card-text class="pb-1">
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex8" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">머리를 감을 때 </span>
                        <span class="surbeyHighlight">머리카락이 많이 빠지고</span>
                        <span class="surbeyNomal"> 머리숱이 없어 보인다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex9" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">두피 색</span>
                        <span class="surbeyNomal">이 </span>
                        <span class="surbeyHighlight">붉거나 뾰루지</span>
                        <span class="surbeyNomal">가 자주 생긴다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex10" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">두피에 </span>
                        <span class="surbeyHighlight">기름(지성, 지루성, 냄새)이 많이 생긴다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex11" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">스트레스가 많은 일을 하고, </span>
                        <span class="surbeyHighlight">스트레스를 받으면 잘 풀지 못한다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex12" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">술을 자주</span>
                        <span class="surbeyNomal"> 마신다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex13" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyNomal">피로를 자주 느끼고 </span>
                        <span class="surbeyHighlight">목과 등 근육이 뻐근</span>
                        <span class="surbeyNomal">하며 잘 풀리지 않는다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex14" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">염색</span>
                        <span class="surbeyNomal">을 </span>
                        <span class="surbeyHighlight">자주</span>
                        <span class="surbeyNomal"> 한다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row class="pb-0 text-right">
                <v-col class="pb-0 text-right" style="font-family: 'Noto Serif KR', serif; color: gray">출처: 대한탈모치료학회</v-col>
              </v-row>
            </v-card-text>
          
          </v-card>
          <div class="text-right">
            <v-btn 
              @click="e1 = 1"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              이 전
            </v-btn>
            <v-btn
              color="primary"
              @click="e1 = 3"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>
        </v-stepper-content>
  
        <v-stepper-content step="3" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">설문조사 (3/3)</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
          >
            <v-card-text class="pb-1">
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex15" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div class="surbeyHighlight">
                        <span class="surbeyNomal">평소 </span>
                        <span class="surbeyHighlight">젤과 스프레이</span>
                        <span class="surbeyNomal"> 등을 많이 사용한다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex16" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">인스턴트 음식</span>
                        <span class="surbeyNomal">이나 패스트푸드를 </span>
                        <span class="surbeyHighlight">자주 먹는다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex17" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">면류나 기름기</span>
                        <span class="surbeyNomal"> 있는 음식을 즐긴다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex18" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">해조류와 채소, 과일을 거의 먹지 않는다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex19" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">매일 담배</span>
                        <span class="surbeyNomal">를 피운다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-checkbox 
                    v-model="checkbox_result.ex20" 
                    hide-details
                  >
                    <template v-slot:label>
                      <div>
                        <span class="surbeyHighlight">생활이 불규칙적</span>
                        <span class="surbeyNomal">이고 밤늦게까지 잠을 못자고 </span>
                        <span class="surbeyHighlight">수면량이 적은 편</span>
                        <span class="surbeyNomal">이다.</span>
                      </div>
                    </template>
                  </v-checkbox>
                </v-col>
              </v-row>
              <v-row class="pb-0 text-right">
                <v-col class="pb-0 text-right" style="font-family: 'Noto Serif KR', serif; color: gray">출처: 대한탈모치료학회</v-col>
              </v-row>
            </v-card-text>
          </v-card>
          <div class="text-right">
            <v-btn 
              @click="e1 = 2"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              이 전
            </v-btn>
            <v-btn
              color="primary"
              @click="e1 = 4"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>
        </v-stepper-content>


        <v-stepper-content step="4" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">AI 카메라 (1/1)</div>
          <!-- 사진 업로드 안했을 때 -->
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="!imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center" class="mx-0">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <input ref="imageInput" type="file" hidden @change="onChangeImages">
                  <v-img
                    src="../../assets/11.png"
                    class="testSample"
                    @click="onClickImageUpload"
                    style="cursor:pointer;"
                    width="200px"
                  ></v-img>                   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large;">이미지를 업로드해주세요</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="!imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              disabled
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>

          <!-- 사진 업로드 후 -->
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <v-img 
                    :src="imageUrl" 
                    cover
                    @click="onClickImageUpload" 
                    style="cursor:pointer;"
                    width="200px"
                  >
                  </v-img>
                  <input ref="imageInput" type="file" hidden @change="onChangeImages">               
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large">이미지를 업로드해주세요.</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              @click="upload"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>
        </v-stepper-content>


        <v-stepper-content step="5" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">채점중..</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            v-if="imageUrl" 
          >
            <v-card-text>
              <v-row
                align="center"
                justify="center"
                class="mx-2 mt-3"
              > 
                <v-col justify="center" align="center">
                  <span class="surbeyHighlight" style="font-size: x-large">정수리</span>
                  <span class="surbeyNomal" style="font-size: large"> 또는</span>
                  <span class="surbeyHighlight" style="font-size: x-large"> 이마가 드러난 사진</span>
                  <span class="surbeyNomal" style="font-size: large">을</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col justify="center" align="center" class="pt-0">
                  <span class="surbeyNomal" style="font-size: large"> 올려주세요!</span>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  align="center" 
                  justify="center"
                >
                  <v-img 
                    :src="imageUrl" 
                    cover
                    style="cursor:pointer;"
                    width="200px"
                  >
                    <div class="text-center">
                      <v-progress-circular
                        :size="130"
                        :width="15"
                        color="primary"
                        indeterminate
                      >채점중</v-progress-circular>
                    </div>
                  </v-img>             
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-center my-3">
                  <span class="surbeyNomal" style="font-size: large">이미지를 업로드해주세요.</span>   
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">
                  <span style="font-family: 'Gamja Flower', cursive; font-size: large; font-weight: bold;">단, 파일명에 한글이 있으면 안됩니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>

          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn
              color="primary"
              disabled
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다 음
            </v-btn>
          </div>
        </v-stepper-content>
        <v-stepper-content step="6" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">테스트 결과(1/2)</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            min-width="300"
          >
            <v-card-text
              class="px-4 text-center"
            > 
              <v-card
                class="mx-auto"
                max-width="300"
                min-width="300"
              >
                <v-toolbar
                  color="blue darken-3"
                  dark
                > 
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">정수리능력시험 성적통지표</v-col>
                </v-toolbar>
                <v-row style="margin: auto;">
                  <v-col cols="3" 
                    class="pb-0 pl-0 pr-0 pt-0" 
                    style="border-top-style: solid; border-top-color: white; 
                          border-bottom-style: solid; border-bottom-color: white; color: white;
                          border-right-style: solid;
                          border-right-color:white;"
                  >

                    <v-img 
                      :src="imageUrl" 
                      cover
                      style="cursor:pointer;"
                      min-width="64px"
                      max-height="95px"
                      height="100%"
                    ></v-img>  

                  </v-col>
                  <v-col cols="9" class="pb-0 pl-0 pr-0 pt-0">
                    <v-row style="margin: auto; background-color: gray;">
                      <v-col 
                        class="resultText" 
                        style="border-top-style: solid; border-top-color: white; border-bottom-style: solid; border-bottom-color: white; color: white;">
                        닉네임
                      </v-col>
                    </v-row>
                    <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                      <v-col class="resultText" style="background-color: lightgray;">{{ nickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">구분</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">정수리 영역</v-col>
                </v-row>
                <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                  <v-col cols="3" class="resultBorder">점수</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ result }} 점</v-col>
                </v-row>
                <v-row style="margin: auto;">
                  <v-col cols="3" class="resultBorder">등급</v-col>
                  <v-col class="resultText" style="background-color: lightgray;">{{ grade }} 등급</v-col>
                </v-row>
              </v-card>
              <v-row>
                <v-col class="pb-0 pt-5" style="font-family: 'Jua', sans-serif; font-size: large;">{{ this.nowDate }}</v-col>
              </v-row>
              <v-row class="mb-5">
                <v-col class="pt-0" style="font-family: 'Jua', sans-serif; font-size: large;">정수리영역평가원장</v-col>
              </v-row>
              <v-row v-if="grade < 4" class="gradeResult1 text-left" style="margin: auto;">                
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">3등급 이하</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">아직 안전한 단계</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large; color: white">두피를 청결하게 유지</span>
                  <span style="font-size: large;">하고 좋은 생활 습관을 통해 탈모를 예방하세요.</span>
                </v-col>
              </v-row>
              <v-row v-else-if="grade < 7" class="gradeResult2 text-left" style="margin: auto;"> 
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">4~6등급</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">탈모 초기 증상</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large;">빨리 전문적인 진료를 받아 </span>  
                  <span style="font-size: large; color: white">적극적인 탈모/투피 치료</span>
                  <span style="font-size: large;">를 받으셔야 조기 예방, 개선할 수 있습니다.</span>
                </v-col>
              </v-row>
              <v-row v-else-if="grade < 10" class="gradeResult3 text-left" style="margin: auto;">
                <v-col cols="4">
                  <v-row><v-col class="pr-0 pb-0" style="font-size: x-large; color: white">7등급 이상</v-col></v-row>
                  <v-row><v-col class="pr-0 pt-1" style="font-size: large;">탈모 진행 중</v-col></v-row>
                </v-col>
                <v-col cols="8">
                  <span style="font-size: large;">정확한 진단 후 </span>
                  <span style="font-size: large; color: white">탈모 전문 치료</span>
                  <span style="font-size: large;">를 받으셔야 더 이상의 악화 현상을 받지할 수 있습니다.</span>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn
              class="mb-1"
              color="primary"
              @click="e1 = 7"
              style="margin-right: 10px; font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              미래 예상
            </v-btn>
          </div>
        </v-stepper-content>
        <v-stepper-content step="7" class="pt-1">
          <div class="pt-1 pb-4 text-right surbeyTitle">테스트 결과(2/2)</div>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            min-width="300"
            v-if="grade < 4"
          >
            <v-card-text
              class="px-4 text-center"
            > 
              <v-card
                class="mx-auto"
                max-width="400"
              >
                <v-toolbar
                  color="blue darken-3"
                  dark
                > 
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">{{ grade }}등급의 예상 증명사진</v-col>
                </v-toolbar>
                <v-row style="margin: auto;">
                  <v-img 
                    src="../../assets/hairloss4.gif" 
                    cover
                    style="cursor:pointer;"
                    min-width="64px"
                    max-height="500px"
                  ></v-img>
                  <v-col cols="12" class="pb-0 pl-0 pr-0 pt-0">
                    <v-row style="margin: auto; background-color: gray;">
                      <v-col 
                        class="resultText" 
                        style="border-bottom-style: solid; border-bottom-color: white; color: white;">
                        닉네임
                      </v-col>
                    </v-row>
                    <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                      <v-col class="resultText" style="background-color: lightgray;">{{ nickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card>
            </v-card-text>
          </v-card>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            min-width="300"
            v-else-if="grade < 7"
          >
            <v-card-text
              class="px-4 text-center"
            > 
              <v-card
                class="mx-auto"
                max-width="400"
              >
                <v-toolbar
                  color="blue darken-3"
                  dark
                > 
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">{{ grade }}등급의 예상 증명사진</v-col>
                </v-toolbar>
                <v-row style="margin: auto;">
                  <v-img 
                    src="../../assets/hairloss5.gif" 
                    cover
                    style="cursor:pointer;"
                    min-width="64px"
                    max-height="500px"
                  ></v-img>
                  <v-col cols="12" class="pb-0 pl-0 pr-0 pt-0">
                    <v-row style="margin: auto; background-color: gray;">
                      <v-col 
                        class="resultText" 
                        style="border-bottom-style: solid; border-bottom-color: white; color: white;">
                        닉네임
                      </v-col>
                    </v-row>
                    <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                      <v-col class="resultText" style="background-color: lightgray;">{{ nickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card>
            </v-card-text>
          </v-card>
          <v-card
            class="mb-12"
            color="brown lighten-5"
            min-width="300"
            v-else-if="grade < 10"
          >
            <v-card-text
              class="px-4 text-center"
            > 
              <v-card
                class="mx-auto"
                max-width="400"
              >
                <v-toolbar
                  color="blue darken-3"
                  dark
                > 
                  <v-col style="font-family: 'Jua', sans-serif; font-size: x-large">{{ grade }}등급의 예상 증명사진</v-col>
                </v-toolbar>
                <v-row style="margin: auto;">
                  <v-img 
                    src="../../assets/hairloss6.gif" 
                    cover
                    style="cursor:pointer;"
                    min-width="64px"
                    max-height="500px"
                  ></v-img>
                  <v-col cols="12" class="pb-0 pl-0 pr-0 pt-0">
                    <v-row style="margin: auto; background-color: gray;">
                      <v-col 
                        class="resultText" 
                        style="border-bottom-style: solid; border-bottom-color: white; color: white;">
                        닉네임
                      </v-col>
                    </v-row>
                    <v-row style="margin: auto; border-bottom-style: solid; border-bottom-color: white;">
                      <v-col class="resultText" style="background-color: lightgray;">{{ nickname }}</v-col>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card>
            </v-card-text>
          </v-card>
          <div 
            v-if="imageUrl" 
            class="text-right"
          >
            <v-btn 
              class="mr-4 mb-1"
              @click="reset()"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
            >
              다시하기
            </v-btn>
            <v-btn
              class="mb-1"
              color="primary"
              style="font-family: 'Gothic A1', sans-serif; font-size: small; font-weight: bold;"
              @click="e1 = 6"
            >
              이 전
            </v-btn>
          </div>
        </v-stepper-content>          
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      // count: this.$route.params.count,
      files: [],
      imageUrl: '',
      selected: false,
      result: 100,
      searched: false,
      score: 0,
      uploadId: null,
      nowDate: null,
      nickname: null,
      grade: 1,
      isloading: false,
      //
      e1: 1,
      page: 1,
      checkbox: true,
      checkbox_result: {
        "ex1" : false,
        "ex2" : false,
        "ex3" : false,
        "ex4" : false,
        "ex5" : false,
        "ex6" : false,
        "ex7" : false,
        "ex8" : false,
        "ex9" : false,
        "ex10" : false,
        "ex11" : false,
        "ex12" : false,
        "ex13" : false,
        "ex14" : false,
        "ex15" : false,
        "ex16" : false,
        "ex17" : false,
        "ex18" : false,
        "ex19" : false,
        "ex20" : false,
      },
      count: 0,
    }
  },
  created() {
    let today = new Date();
    let year = today.getFullYear()
    let month = today.getMonth() + 1
    let date = today.getDate()

    this.nowDate = `${year}.${month}.${date}`
    const token = sessionStorage.getItem('token')
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/api/accounts/user/`, 
      {
        headers: {Authorization: `token ${token}`}
      }
    )
    .then((re) => {
      this.user_id = re.data.id
      this.nickname = re.data.nickname
    })
    .catch(() => {})
  },
  methods: {
    clickSubmit() {
      // api로 결과 post
      // 리턴된 값을
      for (let key in this.checkbox_result) {
        if (this.checkbox_result[key] === true) {
          this.count += 1
        }
      }
    },
    clickNext() {
      this.page += 1
    },
    clickPrevious() {
      this.page -= 1
    },
    reset() {
      this.$router.push({ name: 'InitSurvey'})
    },

    upload() {
      this.clickSubmit()
      this.isloading = true
      this.searched = true
      this.e1 = 5
      this.score = parseInt((210-(this.count * (this.count +1)) / 2) * (5/21))
      let fd = new FormData();
      fd.append('files', this.files)
      let token = sessionStorage.getItem('token')
      axios.post('/api/api/images/analyze-image/',
        fd, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `token ${token}`,
          }
        }
      ).
      then((res) => {
        // console.log('upload res', res)
        this.result = parseInt((100-res.data.result)/2) + this.score
        this.searched = true
        this.isloading = false
        this.e1 = 6
        this.uploadId = res.data.image.id
        if (this.result == 100) {
          this.grade = 1
        } else if (this.result < 10) {
          this.grade = 9
        } else {
          this.grade = 10 - parseInt(this.result / 10)
        }
        this.saveResult()
      })
      .catch(() => {
        
        this.e1 = 4
        alert('파일명이 한글입니다. 영어로 변경해 주세요.')
      });
    },
    saveResult() {
      let token = sessionStorage.getItem('token')
      axios.post('/api/api/images/save-score/', {'image': this.uploadId, 'score': this.result}, {
        headers: {
          'Authorization': `token ${token}`,
        }
      })
        .then(() => {
          // console.log('saveResult', res)
        })
    },
    onClickImageUpload() {
      this.selected = true
      this.$refs.imageInput.click()
    },
    onChangeImages(e) {
      this.files = e.target.files[0]
      let nameLength = e.target.files[0].name.length
      let verifyFile = e.target.files[0].name.slice(nameLength-3, nameLength) 
      if (verifyFile == 'PNG' || verifyFile == 'jpg' || verifyFile == 'png' || verifyFile == 'JPG') {
        this.imageUrl = URL.createObjectURL(this.files)
      } else {
        alert('jpg 또는 PNG 파일형식만 가능합니다.')
        return false
      }
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR&family=Do+Hyeon&family=Nanum+Gothic&family=Noto+Sans+KR:wght@900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

.surbeyHighlight {
  color:#FFAB00;
  font-family: 'Do Hyeon', sans-serif;

}

.surbeyNomal {
  font-family: 'Do Hyeon', sans-serif;
}

.surbeyTitle {
font-family: 'Noto Sans KR', sans-serif;
font-weight: 900;
}

.testSample {
  border: 3px solid gold;
  border-radius: 220px;
  -moz-border-radius: 220px;
  -khtml-border-radius: 220px;
  -webkit-border-radius: 220px;
}

.resultBorder {
  margin: auto;
  border-right-style: solid;
  border-right-color:white;
  width: 20px !important;
  background-color: gray;
  color: white;
  font-family: 'Jua', sans-serif;
  font-size: large
}

.resultText {
  font-family: 'Jua', sans-serif;
  font-size: large;
}

.gradeResult1 {
  background-color: #ffbe73;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.gradeResult2 {
  background-color: #fd9463;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.gradeResult3 {
  background-color: #ff5953;
  align-items: center;
  font-family: 'Jua', sans-serif;
  max-width: 400px;
}

.v-progress-circular {
  margin: 1rem;
}

.v-progress-circular__info {
  /* color: rgb(0, 16, 85); */
  color: white;
  font-weight: 550;
  font-size: xx-large;
  font-family: 'Jua', sans-serif;
}


</style>