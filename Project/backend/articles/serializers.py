from django.contrib.auth import get_user_model
from rest_framework import serializers
# from django.contrib.auth.model import User
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.username
    def get_nickname(self, obj):
        return obj.user.nickname
    username = serializers.SerializerMethodField('get_username')
    nickname = serializers.SerializerMethodField('get_nickname')

    class Meta:
        model = Comment
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    def get_username(self, obj):
        return obj.user.username
    def get_nickname(self, obj):
        return obj.user.nickname
    username = serializers.SerializerMethodField('get_username')
    nickname = serializers.SerializerMethodField('get_nickname')
    comment = CommentSerializer(many=True, read_only=True)
    image = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

