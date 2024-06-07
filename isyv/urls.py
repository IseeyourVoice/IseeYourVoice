from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),  # 게시판 URL 추가
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('post/<int:post_id>/comment/', views.create_comment, name='create_comment'),
    path('soundedit/', views.soundedit, name='soundedit'),
    path('soundedit_download/', views.soundedit_download, name='soundedit_download'),
]
