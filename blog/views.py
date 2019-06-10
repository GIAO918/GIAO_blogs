from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from blog import forms
from blog import models
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def love(request):
    return render(request, '521.html')


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

    # category_list = models.Category.objects.filter(blog=blog)

    # 利用分组查询，查看每个用户下有多少文章分类，并把这些分类下有多少文章计算出来

    category_list = models.Category.objects.filter(blog=blog).annotate(a=Count("article"))
    # 这里前半部分获取的是当前用户下共有多少分类，.annotate把这些分类分组，求出每个分组下共有多少文章，最后的filter
    # 过滤掉文章数等于0的分组

    tag_list = models.Tag.objects.filter(blog=blog).annotate(a=Count("article")).filter(a__gt=0)

    # 按日期给用户的文章进行归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive").annotate(c=Count("nid")).values("archive", 'c')

    return render(request, "home.html", {
        "user":user,
        "blog": blog,
        "article_list": article_list,
        "category_list": category_list,
        "tag_list": tag_list,
        "archive_list": archive_list})

# 定义一个函数，得到个人博客左侧页面的数据
def get_left_menu(user,blog):
    category_list = models.Category.objects.filter(blog=blog).annotate(a=Count("article"))
    tag_list = models.Tag.objects.filter(blog=blog).annotate(a=Count("article")).filter(a__gt=0)
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive").annotate(c=Count("nid")).values("archive", 'c')
    return category_list,tag_list,archive_list

def article_detail(request, username,pk):  # 跳转到文章详情页
    print(username,pk)
    user = models.UserInfo.objects.filter(username = username).first()  # 查询出用户对象
    blog = user.blog
    article_obj = models.Article.objects.filter(nid=pk).first()
    category_list,tag_list,archive_list = get_left_menu(user,blog)

    return render(request,"article_detail.html",
                  {"article":article_obj,
                   "blog":blog,
                   "category_list":category_list,
                   "tag_list":tag_list,
                   "archive_list":archive_list
                   })