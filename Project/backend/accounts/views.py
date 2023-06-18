from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import update_last_login

from allauth.account.views import SignupView

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import *
from articles.models import *
from articles.serializers import *
from images.models import *
from images.serializers import *

from knox.models import AuthToken

from django.db.models import Q

import string
import random
from django.core.mail import send_mail

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    User = get_user_model()
    def post(self, request, *args, **kwargs):
        body = {}
        try:    
            User.objects.get(username=request.data["username"])
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data
                update_last_login(None, user)       #최근 로그인 시간 저장    
                u_last_login = user.last_login
                up_last_login = u_last_login.strftime('%Y-%m-%d %H:%M:%S')
                user.last_login = up_last_login
                return Response(
                    {
                        "user": UserSerializer(
                            user, context=self.get_serializer_context()
                        ).data,
                        "token": AuthToken.objects.create(user)[1],
                    }
                )
            else:
                user = User.objects.get(username=request.data["username"])
                serializer = UserSerializer(user)
                data = serializer.data
                body["error"] = { "password" : "비밀번호가 일치하지 않습니다."}
                return Response(body)
        except: # ID 없음
            body["error"] = {
                "username": "아이디 정보가 없습니다."
                }
            return Response(body)
        

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    User = get_user_model()
    def get(self, request, *args, **kwargs):
        body = {}
        username=request.GET.get("username")
        serializer=UserSerializer(User.objects.filter(Q(username=username)), many=True)
        if serializer.data:
            return Response({'error': '해당 아이디는 이미 존재합니다.'})
        return Response({'message': '중복된 아이디가 없습니다. 사용할 수 있는 아이디입니다.'})

    def post(self, request, *args, **kwargs):
        body = {}
        try:    # 이미 가입된 ID인지 확인
            User.objects.get(username=request.data["username"])
            body["error"] = {
                        "username": "해당 아이디는 이미 존재합니다."
                    }
            return Response(body)
        except: # 아이디 & 비밀번호 제한조건 확인
            if len(request.data["username"]) < 6:
                body["error"] = {
                        "username": "아이디는 6자리 이상이어야 합니다."
                    }
                return Response(body)
            if len(request.data["password"]) < 8:
                body["error"] = { "password" : "비밀번호는 8자리 이상이어야 합니다." }
                return Response(body)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        update_last_login(None, user)       #최근 로그인 시간 저장    
        u_last_login = user.last_login
        up_last_login = u_last_login.strftime('%Y-%m-%d %H:%M:%S')
        user.last_login = up_last_login
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

####  회원 탈퇴, 정보 수정, 정보 보기 #####
class UserProfileAPI(generics.GenericAPIView):
    User = get_user_model()
    serializer_class = UserSerializer, HairImageSerializer, ArticleSerializer, ComposeImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    ### 회원 정보 보기
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        images = HairImage.objects.filter(upload_user=request.user)
        compose_images = ComposeImage.objects.filter(upload_user=request.user)
        article = Article.objects.filter(user=request.user)
        article_serializer = ArticleSerializer(article, many=True)
        image_serializer = HairImageSerializer(images, many=True)
        user_serializer = UserSerializer(user)
        compose_serializer = ComposeImageSerializer(compose_images, many=True)
        data = user_serializer.data
        data["images"] = image_serializer.data
        data["articles"] = article_serializer.data
        data['compose'] = compose_serializer.data
        return Response(data)

    ### 회원 정보 수정
    def put(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user.nickname = request.data['nickname']
        user.save()
        serializer = UserSerializer(user)
        return Response({'message': '성공적으로 수정하였습니다.', 'content': serializer.data})
    ### 회원 탈퇴
    def delete(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user.delete()
        return Response({'message': '성공적으로 탈퇴하였습니다.'})
 

def email_auth_num(): # 랜덤 10자리 생성
    LENGTH = 10
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num

def contents(new_password,nickname,email):
    char = nickname+"("+email+")"+"님의 새로운 비밀번호는 "+"'"+new_password +"'" + " 입니다."
    return char

### 비밀번호 찾기
class SmtpAPI(generics.GenericAPIView):
    User = get_user_model()
    serializer_class = PassSerializer
    def put(self, request, *args, **kwargs):
        email = request.data['email']
        username = request.data['username']
        if User.objects.filter(username=username).exists():
            user = get_object_or_404(User, username=username)
            if user.email == email:
                new_password = email_auth_num() # 새로운 비밀번호
                user.set_password(new_password)
                user.save()
                send_mail(
                    '안녕하십니까 모난사람에서 새로 발급한 비밀번호 입니다.', 
                    contents(new_password,user.username,email),
                    'dmswo708@naver.com',
                    [str(email)],
                    fail_silently=False,
                    )
                return Response({'message':'메일로 새로운 비밀번호를 전송했습니다. 메일을 확인해주세요.'})

            return Response({'message':'메일을 정확히 입력해주세요.'})
        else:
            return Response({'message':'아이디를 정확히 입력해주세요.'})

### 비밀번호 변경
@permission_classes([IsAuthenticated])
class profileAPI(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    User = get_user_model()
    def put(self, request, *args, **kwargs):
        username = request.data['username']
        current_pw = request.data['password']
        new_pw1 = request.data['newpassword']
        new_pw2 = request.data['checkpassword']
        try:
            user = User.objects.get(username=username)
            if user == request.user:
                if check_password(current_pw, user.password):
                    if new_pw1 == new_pw2:
                        user.set_password(new_pw1)
                        user.save()
                        serializer = UserSerializer(instance=user)
                        return Response({'message' : 'Success', 'user': serializer.data})
                    else:
                        return Response({'error' : '새로운 비밀번호를 확인해 주세요.'})
                else:
                    return Response({'error' : '기존 비밀번호를 확인해 주세요.'})
        except:
            return Response({'error' : '회원 정보가 존재하지 않습니다.'})