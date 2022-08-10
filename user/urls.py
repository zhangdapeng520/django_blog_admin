from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 注册
    path('register/', views.register, name='register'),
    # 登录
    path('login/', views.login_view, name="login"),
    # 注销
    path('logout/', views.logout_view, name="logout"),
]
