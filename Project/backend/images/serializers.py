from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import *

class HairImageSerializer(serializers.ModelSerializer):
    upload_user = UserSerializer(required=False) # user의 pk 값만 나오기 때문에 UserSerializer 이용
    class Meta:
        model = HairImage
        fields = '__all__'
class ComposeImageSerializer(serializers.ModelSerializer):
    upload_user = UserSerializer(required=False) # user의 pk 값만 나오기 때문에 UserSerializer 이용
    class Meta:
        model = ComposeImage
        fields = '__all__'