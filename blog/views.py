from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from blog import forms
from blog import models

from django.contrib.auth.decorators import login_required


# 注册功能视图
def register(request):
    if request.method == "POST":
        form_obj = forms.RegForm(request.POST)
        if form_obj.is_valid():
            # 如果校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
            return HttpResponse("注册成功")
        else:
            return render(request, "register.html", {"form_obj": form_obj})

    form_obj = forms.RegForm()  # 生成form对象
    return render(request, "register.html", {"form_obj": form_obj})


def login_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 判断用户名密码是否正确
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, "index.html")
        else:
            return HttpResponse("登录失败")
    return render(request, "login.html")


def logout_view(request):
    logout(request)  # 已经封装了用户的request
    return redirect("/login/")


def index(request):
    article_list = models.Article.objects.all()
    return render(request, "index.html", {'article_list': article_list})


# 返回个人主页的视图
def home(request, username=None):
    user = models.UserInfo.objects.filter(username=username).first()
    if user:
        blog = user.blog
    else:
        return HttpResponse("404")

    article_list = models.Article.objects.filter(user=user)

    category_list = models.Category.objects.filter(blog=blog)
    # 利用分组查询，查看每个用户下有多少文章分类，每个分类有多少文章
    # from django.db.models import Count
    # ret = models.Category.objects.filter(blog=blog).annotate(a=Count("article")).filter("title", "a")
    # print(ret)
    return render(request, "home.html", {"blog": blog, "article_list": article_list, "category_list": category_list})
