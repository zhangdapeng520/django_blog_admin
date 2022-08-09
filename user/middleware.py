from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from blog_admin import settings


class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 获取当前路径
        current_path = request.path
        print("当前路径", current_path)

        # 登录，注册，注销，都不用校验
        if current_path in ['/user/login/', '/user/register/']:
            return

        # 登录校验
        if not settings.username:
            return redirect(reverse('user:login'))
