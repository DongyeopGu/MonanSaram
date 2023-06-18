from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('article/', views.create_article),
    path('article/<int:article_pk>/',views.article_detail),
    path('article/<int:article_pk>/comment_create/',views.comment_create),
    path('article/<int:article_pk>/<int:comment_pk>/comment_update/',views.comment_update_and_delete),
    path('article/<int:article_pk>/image-delete/', views.delete_image),
    path('article/<int:article_pk>/recommendation/', views.recommendation)
    # path('comment_list/', views.comment_list)
]