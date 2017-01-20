from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.learning_centre_overview),
    url(r'articles/$', views.article_overview, name="articles"),
    url(r'^videos/$', views.video_overview, name="videos"),
    url(r'^courses/$', views.course_overview, name="courses"),
    url(r'^(?P<slug>[-\w]+)/$', views.article_detail, name="article"),
    url(r'^(?P<slug>[-\w]+)/$', views.video_detail, name="video"),
    url(r'^courses/(?P<slug>[-\w]+)/$', views.course_detail, name="course"),
]
