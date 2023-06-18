from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "nickname", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None,validated_data["password"]
        )
        user.email = validated_data["email"]
        user.nickname = validated_data['nickname']
        user.save()
        return user

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class PasswordChangeSerializer(serializers.ModelSerializer):
    newpassword = serializers.CharField()
    checkpassword = serializers.CharField()
    class Meta:
        model = User
        fields = ('username','password','newpassword','checkpassword')