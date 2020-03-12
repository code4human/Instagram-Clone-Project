from django.urls import path
from .views import *  #뷰에 있는 모든 함수

app_name = 'post'

urlpatterns = [
    path('', post_list, name='post_list'),  #instagram\urls.py에서 post를 미리 잡아줬으므로 빈칸
    path('new', post_new, name='post_new'),
    path('edit/<int:pk>/', post_edit, name='post_edit'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),

    path('like', post_like, name='post_like'),
    path('bookmark', post_bookmark, name='post_bookmark'),

    path('comment/new', comment_new, name='comment_new'),
    path('comment/delete', comment_delete, name='comment_delete'),
]

