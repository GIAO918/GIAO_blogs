from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r"^up_down$",views.is_up),
    url(r"^comment$",views.comment),
    url(r"^(\w+)/article/(\d+)$",views.article_detail),   # 文章详情
    url(r"^(?P<username>\w+)/(?P<i>\w+)",views.ret_tags),
    url(r"(?P<username>\w+)",views.home),   # 个人主页

]