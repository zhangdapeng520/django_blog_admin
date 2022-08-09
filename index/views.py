from django.shortcuts import render, redirect
from django.urls import reverse

from blog_admin import settings


def index(request):
    """
    首页视图函数
    :param request:
    :return:
    """
    # 登录校验
    # if not settings.username:
    #     return redirect(reverse('user:login'))

    context = {"username": settings.username}
    return render(request, "index.html", context)
