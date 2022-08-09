from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 博客列表
    path('list/', views.blog_list, name='list'),
    # 删除博客
    path('delete/', views.blog_delete, name='delete'),
    # 修改博客
    path('edit/', views.blog_edit, name='edit'),
    # 博客新增
    path('add/', views.blog_add, name='add'),
]
