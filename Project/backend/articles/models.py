from django.db import models
from django.conf import settings
import os
# from accounts.models import User
# Create your models here.

def user_directory_path(instance, filename):
    return 'articles/{0}/{1}'.format(instance.article, filename)

class Category(models.Model):
    category_title = models.CharField(max_length=200, default="")
    
    # def __str__(self):
    #     return self.category_title

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=100)
    content = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)
    recommendation_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommendation_articles',blank=True)     # 추천수
    
    # def __str__(self):
    #     return self.title
class UploadImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='image',null=True)
    image = models.ImageField(upload_to=user_directory_path ,blank=True, null=True)
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(UploadImage, self).delete(*args, **kargs)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    # def __str__(self):
    #     return self.content