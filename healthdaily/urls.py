"""healthdaily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ribao import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article',views.ArticleViewSet)
router.register(r'daily',views.DailyViewSet)
router.register(r'category',views.CategoryViewSet)

urlpatterns = [
    url(r'^callback',views.callback),
    url(r'^sina', views.sina),
    url(r'^justiknow', include(admin.site.urls)),
    url(r'^a/(\d+)', views.article),
    url(r'^addarticle', views.addarticle),
    url(r'^adda', views.adda),
    url(r'^x/(\d+)', views.dailyhomepage),
    url(r'^d/(\d+)', views.daily),
    url(r'^api/',include(router.urls)),
    url(r'^',views.homepage),
]
