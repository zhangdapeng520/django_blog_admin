from django.shortcuts import render, redirect
from django.urls import reverse

from blog_admin import settings
from .models import Blog


def blog_add(request):
    context = {"username": settings.username}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        try:
            Blog.objects.create(title=title, content=content, author_id=settings.user_id)
            return redirect(reverse("blog:list"))
        except Exception as e:
            print(e)
            context["msg"] = "添加博客失败"
            return render(request, "error.html", context)
    return render(request, "blog/add.html", context)


def blog_list(request):
    context = {"username": settings.username}

    # 始终能够优先拿到最新的文章
    blogs = Blog.objects.all().order_by("-id")
    try:
        # 默认是第1页
        page = int(request.GET.get("page", 1))
        # 每页数量
        size = int(request.GET.get("size", 3))
        # 开始索引
        offset = (page - 1) * size
        # 向前端传递
        context['blogs'] = blogs[offset:offset + size]
        return render(request, "blog/list.html", context)
    except Exception as e:
        print(e)
        context['msg'] = "参数错误，请检查page或size的值是否正确"
        return render(request, "error.html", context)


def blog_delete(request):
    context = {}
    blog_id = request.GET.get('id')
    try:
        Blog.objects.get(id=blog_id).delete()
    except:
        context['msg'] = "要删除的数据不存在"
        return render(request, "error.html", context)
    return redirect(reverse('blog:list'))


def blog_edit(request):
    context = {}

    # 执行修改
    if request.method == 'POST':
        blog_id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            blog = Blog.objects.get(id=blog_id)
            blog.title = title
            blog.content = content
            blog.save()
            return redirect(reverse('blog:list'))
        except:
            context['msg'] = "要修改的数据不存在"
            return render(request, "error.html", context)

    # 渲染修改页面
    blog_id = request.GET.get('id')
    try:
        blog = Blog.objects.get(id=blog_id)
        context['blog'] = blog
    except:
        context['msg'] = "要修改的数据不存在"
        return render(request, "error.html", context)
    return render(request, 'blog/edit.html', context)
