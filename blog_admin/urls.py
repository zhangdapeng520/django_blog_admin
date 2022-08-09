from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 后台管理系统的路由
    path('admin/', admin.site.urls),

    # 包含用户应用的子路由
    path('user/', include("user.urls")),
    # 包含博客应用的子路由
    path('blog/', include("blog.urls")),
    path('', include("index.urls")),
]
