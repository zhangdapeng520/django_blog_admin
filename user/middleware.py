from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
import re

class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 获取当前路径
        curr_path = request.path

        # 白名单处理
        white_list = ["/user/register/", "/user/login/"]
        for w in white_list:
            if re.search(w, curr_path):
                return None  # 通过

        # 验证是否登陆
        if not request.user.is_authenticated:
            return redirect(reverse("user:login"))
