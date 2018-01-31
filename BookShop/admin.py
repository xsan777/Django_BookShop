from django.contrib import admin

# Register your models here.
from .models import Classification
class CFAdmin(admin.ModelAdmin):
    list_display = ['cname']
admin.site.register(Classification,CFAdmin)