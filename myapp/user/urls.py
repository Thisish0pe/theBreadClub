from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path("register/", views.Registration.as_view(), name='register'),
    # 로그인
    path("login/", views.Login.as_view(), name='login'),
    # 로그아웃
    # 프로필 보기
    path("profile/", views.ProfileView.as_view(), name="profile"),
    # 프로필 생성
    # 프로필 수정
]