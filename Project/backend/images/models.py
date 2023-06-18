from django.db import models
from django.conf import settings
import os 

# Create your models here.
def user_directory_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.upload_user.username, filename)
def user_path(instance):
    return 'users/{0}'.format(instance.upload_user.username)

class HairImage(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True) # 업로드 시간
    upload_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='hair_user', on_delete=models.CASCADE) # 업로드 유저
    upload_image = models.ImageField(upload_to=user_directory_path, blank=True) # 이미지 경로
    score = models.IntegerField(default=0, null=True)
    def delete(self, *args, **kargs):
        if self.upload_image:
            a = user_path
            img_path = f'{settings.MEDIA_ROOT}/{user_path}'
            os.remove(os.path.join(img_path, self.upload_image.path))
        super(HairImage, self).delete(*args, **kargs)

class ComposeImage(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True) # 업로드 시간
    upload_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='compose_user', on_delete=models.CASCADE) # 업로드 유저
    upload_image = models.ImageField(upload_to=user_directory_path, blank=True) # 이미지 경로
    def delete(self, *args, **kargs):
        if self.upload_image:
            a = user_path
            img_path = f'{settings.MEDIA_ROOT}/{user_path}'
            os.remove(os.path.join(img_path, self.upload_image.path))
        super(ComposeImage, self).delete(*args, **kargs)