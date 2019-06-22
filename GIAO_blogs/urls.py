"""GIAO_blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from blog import views
from blog import urls as blog_urls

from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r"^register", views.register),
    url(r"^login", views.login_in),
    url(r"^logout_view", views.logout_view),

    # 将所有以blog开头的url，都分发给blog这个app下边的urls来处理
    url(r"^blog/", include(blog_urls)),

    # 用户博客图片上传
    url(r"^upload",views.upload),

    # media路由配置
    url(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^", views.index),


]
