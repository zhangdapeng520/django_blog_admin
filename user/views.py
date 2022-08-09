from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from blog_admin import settings


def register(request):
    """
    注册视图函数
    :param request:
    :return:
    """
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        # 用户名和密码校验
        if username == "":
            return render(request, "error.html", {"msg": "用户名不能为空"})
        if password == "":
            return render(request, "error.html", {"msg": "密码不能为空"})
        if len(username) < 3:
            return render(request, "error.html", {"msg": "用户名长度不能小于3"})
        if len(password) < 3:
            return render(request, "error.html", {"msg": "密码长度不能低于6位"})

        # TODO：安全性、数字、字母、大小写、符号

        # 两次密码校验
        if password == re_password:
            try:
                User.objects.create_user(username=username, password=password)
                return redirect(reverse('user:login'))
            except:
                return render(request, "error.html", {"msg": "该用户已存在"})

    return render(request, "user/register.html", context)


def login(request):
    """
    登录视图函数
    :param request:
    :return:
    """
    # 要给前端渲染的数据
    context = {}

    # POST请求，登录校验
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 查有没有用户
        try:
            user = User.objects.get(username=username)
            if user is not None and user.check_password(password):
                # 登录成功以后，跳转到首页
                settings.username = username
                settings.user_id = user.id
                return redirect(reverse("index:index"))
            context["error"] = "用户名或密码错误"
        except:
            context["error"] = "该用户不存在"

    # GET请求：渲染登录页面
    return render(request, "user/login.html", context)


def logout(request):
    """
    注销视图函数
    :param request:
    :return:
    """
    settings.username = ""
    settings.user_id = 1
    return redirect(reverse('user:login'))
