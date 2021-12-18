from django.urls import path
from . import views

app_name = 'blog'
# 블로그 앱의 url에 namespace 설정하도록 변경

urlpatterns = [ # url과 뷰 연결
    path('', views.post_list, name='post_list'),
    # '' : 끝에 blog가 오는 url요청이 오면 post_list뷰로 연결시켜주기
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),  # 삭제 기능
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'), # 댓글 기능
]
