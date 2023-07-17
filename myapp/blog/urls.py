from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 작성하기
    path("write/", views.Write.as_view(), name='write'),
    # 글 상세 조회
    path("detail/<int:pk>/", views.DetailView.as_view(), name='detail'),
    # 글 수정 페이지
    path("detail/<int:pk>/edit/", views.Update.as_view(), name = 'edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)