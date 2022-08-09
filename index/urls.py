from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    # 首页
    path('', views.index, name='index'),
]
