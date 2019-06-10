from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r"article/(\d+)$",views.article_detail),   # 文章详情
    url(r"(?P<username>\w+)",views.home),   # 个人主页
]