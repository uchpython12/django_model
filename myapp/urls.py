from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('other', views.other_view, name='other-view'),  # 注意路径中不带斜杠
    path('', views.home, name='home'),
    path('read/', views.read_data, name='read_data'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
