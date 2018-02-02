from django.contrib import admin
from BookShop.models import *


# Register your models here.
# from .models import Classification

@admin.register(Classification)
class CFAdmin(admin.ModelAdmin):
    cname = Classification.cname
    cname.short_description = '分类名'
    list_display = ['cname']


@admin.register(BookName)
class BNAdmin(admin.ModelAdmin):
    list_display = ['bname', 'cfname']
    exclude = ['bcomment']


@admin.register(Chapter)
class chadmin(admin.ModelAdmin):
    list_display = ['clist', 'ccontent', 'cbook']


@admin.register(Size)
class Size(admin.ModelAdmin):
    list_display = ['size']
@admin.register(Lunbo)
class Lunbo(admin.ModelAdmin):
    list_display = ['img']