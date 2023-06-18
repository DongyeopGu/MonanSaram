from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *
from accounts.serializers import UserSerializer
from .models import *
from accounts.models import *

# Create your views here.

class ArticleList(APIView):
    def get(self, request,*args, **kwargs):        # read
        # print(request.data)
        article = Article.objects.all().order_by('-pk')
        serializer = ArticleSerializer(article, many=True)
        return Response({'articles': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):       # create
    user = request.user
    category = Category.objects.get(category_title=request.data["category"])
    article = Article.objects.create(title=request.data["title"], content=request.data["content"], user=user, category=category)
    print(request.FILES.getlist('files'))
    for img in request.FILES.getlist('files'):
        upload_img = UploadImage.objects.create(image=img, article=article)
    serializer = ArticleSerializer(article)
    return Response({'messgae': '작성완료', "content": serializer.data})
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request,article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    images = UploadImage.objects.filter(article=article)
    comments = Comment.objects.filter(article=article)
    
    if request.method == "GET":
        article.hits += 1
        article.save()
        serializer = ArticleSerializer(article)
        image_serializer = ImageSerializer(images, many=True)
        comment_serializer = CommentSerializer(comments, many=True)
        return Response({"detail": serializer.data, "comments": comment_serializer.data, "images": image_serializer.data})

    elif request.method =="PUT":
        if request.user == article.user:  # account와 merge한뒤 재점검        
            category = Category.objects.get(category_title=request.data["category"])
            article.category = category
            article.title = request.data['title']
            article.content = request.data['content']
            article.save()
            serializer = ArticleSerializer(article)
            if request.FILES != []:
                for img in request.FILES.getlist('files'):
                    upload = UploadImage.objects.create(image=img, article=article)
            return Response({'message': 'Article has been updated!', 'content': serializer.data})
            
        else:
            return Response({'message': '작성자가 아닙니다.'}, status=status.HTTP_403_FORBIDDEN)

    elif request.method =="DELETE":
        if request.user == article.user:  # account와 merge한뒤 재점검
            article.delete()
            return Response({'message':'Article has been deleted!'})
        else:
            return Response({'message': '작성자가 아닙니다.'}, status=status.HTTP_403_FORBIDDEN)
    else: 
        return Response({'message': 'error'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_image(request, article_pk):    
    if request.method =="POST":
        article = get_object_or_404(Article, pk=article_pk)
        temp = request.data['id']
        image = UploadImage.objects.filter(article=article)
        if request.user == article.user: 
            for img_id in temp:
                aa = UploadImage.objects.get(id=img_id)
                aa.delete()
            return Response({'message': '이미지 제거완료'})
        else:
            return Response({'message': '작성자 아닙니다.'})
    else: 
        return Response({'message': 'error'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    user = User.objects.get(username=request.user)
    comment = Comment.objects.create(content=request.data["content"], user=user, article=article)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_and_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk = article_pk)
    user = User.objects.get(username=request.user)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        if request.user == comment.user:  # account와 merge한뒤 재점검
            comment.content = request.data["content"]
            comment.save()
            return JsonResponse({'message':'Comment has been updated!'})
        else:
            return Response({"message": "작성자가 아닙니다."}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user == comment.user:  # account와 merge한뒤 재점검
            comment.delete()
            return JsonResponse({'message':'Comment has been deleted!'})
        else:
            return Response({"message": "작성자가 아닙니다."}, status=status.HTTP_403_FORBIDDEN)
    else:
        return JsonResponse({'message':'error'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendation(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, id=article_pk)
    serializer =ArticleSerializer(article)
    if article.recommendation_users.filter(pk=user.pk).exists():
        article.recommendation_users.remove(user)
        liked = False
    else:
        article.recommendation_users.add(user)
        liked = True
    data = {
        'liked': liked,
        'count': article.recommendation_users.count(),
    }
    return Response(data)