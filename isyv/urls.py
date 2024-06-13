from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),  # 게시판 URL 추가
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('post/<int:post_id>/comment/', views.create_comment, name='create_comment'),
    path('soundedit/', views.fileUpload, name='soundedit'), # 업로드 구현하며 수정, 기존은 views.soundedit
    path('soundedit_download/', views.soundedit_download, name='soundedit_download'),
    path('voice_learning/', views.voice_learning, name='voice_learning'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)