from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r"(?P<username>\w+)",views.home)
]