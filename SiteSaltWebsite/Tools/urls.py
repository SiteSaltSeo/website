from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.feature_overview),
    url(r'^(?P<slug>[-\w]+)/$', views.featured_detail, name="featured"),
]
