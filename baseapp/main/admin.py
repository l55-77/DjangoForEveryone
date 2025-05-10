from django.contrib import admin

# Register your models here.
from django.contrib import admin
# 从当前应用的 models.py 文件中导入 Book 模型
from .models import Book

# Register your models here.
# 将 Book 模型注册到 Django 管理界面
admin.site.register(Book)