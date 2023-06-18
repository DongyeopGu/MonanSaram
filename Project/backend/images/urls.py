from django.urls import path
from . import views

urlpatterns = [
    path('analyze-image/', views.analyze_image),
    path('compose-image/', views.compose_image),
    path('save-score/', views.save_score)
]