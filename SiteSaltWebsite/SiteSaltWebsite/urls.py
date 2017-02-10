"""SiteSaltWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from dashboard import views
from Accounts.views import login_view

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'dinosaurs', views.DinosaurViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('frontend.urls'), name='index'),
    url(r'^login/', login_view, name='login'),
    url(r'^plans/', include('pricing.urls'), name='pricing'),
    url(r'^features/', include('Tools.urls', namespace="features")),
    url(r'^learning-centre/', include('LearningCentre.urls', namespace="learning_centre")),
    url(r'^dinosaurs', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)