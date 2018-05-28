# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Article, Comment

# Register your models here.

def make_reviewed(ModelAdmin,request, queryset):
    queryset.update(is_reviewed=True)
make_reviewed.short_desciption='تغيير حالة المراجعة'





class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','pub_date','is_reviewed']
    list_filter=['author','is_reviewed']
    search_filter=['title','author','body']
    action=[make_reviewed]



admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
