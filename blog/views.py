from django.shortcuts import render,HttpResponse
from blog import forms
from blog import models
# 注册功能视图
def register(request):
    if request.method == "POST":
        form_obj = forms.RegForm(request.POST)
        if form_obj.is_valid():
            # 如果校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            models.UserInfo.objects.create(**form_obj.cleaned_data)
            return  HttpResponse("注册成功")
        else:
            print(form_obj.errors)
            return HttpResponse("注册失败")
    form_obj = forms.RegForm() # 生成form对象

    return render(request,"register.html",{"form_obj":form_obj})