from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<movie_id>[0-9]+)/detail/$',views.detail,name='detail'),
    url(r'^(?P<acto_id>[0-9]+)/acto/$',views.acto,name='acto'),
    url(r'^(?P<directo_id>[0-9]+)/directo/$',views.directo,name='directo'),
    url(r'^about/$',views.about,name='about'),
    url(r'^mov/$',views.mov,name='mov'),
    url(r'^act/$',views.act,name='act'),
    url(r'^dir/$',views.dir,name='dir'),
]
