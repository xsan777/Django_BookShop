from django.contrib import admin
from BookShop.models import *


# Register your models here.
# from .models import Classification
# 分类
@admin.register(Classification)
class CFAdmin(admin.ModelAdmin):
    cname = Classification.cname
    cname.short_description = '分类名'
    list_display = ['cname']


# 图书
@admin.register(BookName)
class BNAdmin(admin.ModelAdmin):
    list_display = ['bname', 'cfname']
    exclude = ['bcomment']


# 章节
@admin.register(Chapter)
class chadmin(admin.ModelAdmin):
    list_display = ['clist', 'ccontent', 'cbook']


# 轮播
@admin.register(Lunbo)
class Lunbo(admin.ModelAdmin):
    list_display = ['img']


# 图书状态
@admin.register(States)
class Lunbo(admin.ModelAdmin):
    list_display = ['state']
