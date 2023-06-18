from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegistrationAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('user/', views.UserProfileAPI.as_view()),
    path('user/pw_update/', views.profileAPI.as_view()),
    path('pw_change/',views.SmtpAPI.as_view()),
]