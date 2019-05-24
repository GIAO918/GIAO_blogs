from django.shortcuts import render, HttpResponse
from django.contrib import auth
from blog import forms
from blog import models


# 注册功能视图
def register(request):
    if request.method == "POST":
        form_obj = forms.RegForm(request.POST)
        if form_obj.is_valid():
            # 如果校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            print(form_obj.cleaned_data)
            models.UserInfo.objects.create(form_obj.cleaned_data)
            return HttpResponse("注册成功")
        else:
            print(form_obj.errors)
            return HttpResponse("注册失败")
    form_obj = forms.RegForm()  # 生成form对象

    return render(request, "register.html", {"form_obj": form_obj})


def login_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 判断用户名密码是否正确
        user = auth.authenticate(username=username, password=password)
        # 将登陆成功的用户信息封装到request.user
        auth.login(request, user)
        print(request.user.username)
        if user:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")
    return render(request, 'login_in.html')
