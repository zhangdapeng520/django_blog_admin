from django.contrib import admin

# 引入定义博客模型
from .models import Blog

# 将模型注册到后台管理系统
admin.site.register(Blog)
