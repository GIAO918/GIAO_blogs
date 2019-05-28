"""
博客网站用的form类
"""

from django import forms


# 定义注册的form类
class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length": "用户名最长是16位",
            "required": "用户名不能为空",

        },
        widget=forms.widgets.TextInput(
            attrs={"class": 'form-control'},  # 给生成的input标签添加 class = form—control属性
        )
    )
    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": 'form-control'},

        ),
        error_messages={
            "min_length": "密码不能小于6位",
            "required": "密码不能为空"
        }
    )
    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": 'form-control'},
        ),
        error_messages={
            "min_length": "密码不能小于6位",
            "required": "密码不能为空"},
    )

    email = forms.EmailField(
        label="邮箱",
        widget=forms.widgets.EmailInput(
            attrs={"class": 'form-control'},
        ),
        error_messages={
            "invalid": "邮箱格式不正确"
        },
    )

    # 重写父类的clean方法
    def clean(self):
        from django.core.exceptions import ValidationError
        pwd = self.cleaned_data.get("password")
        repwd = self.cleaned_data.get("re_password")
        if pwd != repwd:
            self.add_error("re_password", ValidationError("两次密码不一致"))  # 给固定字段添加异常
            raise ValidationError("两次密码不一致")
        return self.cleaned_data
