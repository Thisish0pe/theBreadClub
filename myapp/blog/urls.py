from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 작성하기
    path("write/", views.Write.as_view(), name='write'),
    # 글 상세 조회
    path("detail/<int:pk>/", views.DetailView.as_view(), name='detail'),
    # 글 수정 페이지
    path("detail/<int:pk>/edit/", views.Update.as_view(), name = 'edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name='delete'),
    # 검색 기능
    path("search/" ,views.Search.as_view(), name='search'),
    # 댓글 작성
    path("detail/<int:pk>/comment/write", views.CommentWrite.as_view(), name='cm-write'),
    # 댓글 수정
    path("detail/<int:pk>/comment/edit/", views.CommentUpdate.as_view(), name='cm-edit'),
    # 댓글 삭제
    path("detail/<int:pk>/comment/delete/", views.CommentDelete.as_view(), name='cm-delete'),
]