from django.conf.urls import url
from . import views

app_name = 'newsapp'
urlpatterns = [
    url(r'^$' , views.list),
    url(r'^list/$', views.list),
    url(r'^(?P<article_id>\d+)/show/$', views.show, name='show'),
    url(r'^(?P<article_id>\d+)/comment/$', views.comment, name='comment'),

]
