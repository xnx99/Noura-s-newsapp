# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=80)
    title = models.CharField(max_length=200, default='First Title')
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField('تاريخ النشر',auto_now_add=True)
    is_reviewed= models.BooleanField(verbose_name="هل تمت المراجعة؟",default=False)

#to make it in arabic user friendly
    class Meta:
        verbose_name='مقالة'
        verbose_name_plural='مقالات'

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article)
    author = models.CharField(max_length=80)
    text = models.TextField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)



