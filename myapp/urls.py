from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # 引入内建的认证视图

urlpatterns = [
    # path('', views.index, name='index'),
    path('other', views.other_view, name='other-view'),  # 注意路径中不带斜杠
    path('', views.home, name='home'),
    path('read/', views.read_data, name='read_data'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 登出的 URL 配置
]
