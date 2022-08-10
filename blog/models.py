from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# 自定义验证器，最低长度不小于30
content_validator = MinLengthValidator(limit_value=30, message="文章的长度不能小于30个字符")


class Blog(models.Model):
    """
    博客模型
    """
    # 标题
    title = models.CharField(max_length=250)  # varchar

    # 内容
    content = models.TextField(validators=[content_validator])  # text

    # 点赞数量
    good_num = models.IntegerField(default=0)

    # 踩数量
    bad_num = models.IntegerField(default=0)

    # 阅读数量
    view_num = models.IntegerField(default=0)

    # 发布时间
    date_published = models.DateTimeField(default=timezone.now)  # datetime

    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 级联删除

    def __str__(self):
        return self.title
