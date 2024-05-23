from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'common'
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'common/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('soundedit/', views.soundedit, name='soundedit'),
    path('soundedit_download/', views.soundedit_download, name='soundedit_download'),
]