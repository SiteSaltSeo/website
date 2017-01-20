from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.overall, name='plan'),
    url(r'^/plans/(?P<slug>[-\w]+)/$', views.individual, name='plans'),
 
]
