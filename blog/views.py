from django.shortcuts import render
from blog import forms

# 注册功能视图
def register(request):
    form_obj = forms.RegForm()
    return render(request,"register.html",{"form_obj":form_obj})