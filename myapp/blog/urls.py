from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 작성하기
    path("write/", views.Write.as_view(), name='write'),
]