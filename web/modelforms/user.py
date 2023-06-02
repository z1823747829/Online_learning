import re

from django import forms
from django.core.exceptions import ValidationError

from web.models.user import User
from web.utils.tools import md5_salt


class SigninModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['uname', 'password']

    def clean_password(self):
        return md5_salt(self.cleaned_data.get("password"))


class SignupModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="确认密码")

    class Meta:
        model = User
        fields = ['nickname', 'uname', 'password', 'confirm_password']

    def clean_uname(self):
        uname = self.cleaned_data["uname"]
        pattern = re.compile(r"^[a-zA-Z0-9_]{1,32}$")
        if not pattern.match(uname):
            raise ValidationError("用户名应由字母，数字，下划线组成，1-32位")
        elif User.objects.filter(uname=uname).exists():
            raise ValidationError("用户名已存在")
        return uname

    def clean_password(self):
        password = self.cleaned_data["password"]
        pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]{6,64}$")
        if not pattern.match(password):
            raise ValidationError("密码应由字母，数字，特殊字符组成，至少包含字母和数字，6-64位")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data["confirm_password"]
        if not password:
            return confirm_password
        if password != confirm_password:
            raise ValidationError("密码不一致")
        return confirm_password


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', ]

    def clean_uname(self):
        uname = self.cleaned_data["uname"]
        pattern = re.compile(r"^[a-zA-Z0-9_]{1,32}$")
        if not pattern.match(uname):
            raise ValidationError("用户名应由字母，数字，下划线组成，1-32位")
        return uname

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if phone == '' or phone == 'null' or phone is None:
            return ''
        pattern = re.compile(r"1\d{10}")
        if not pattern.match(phone):
            raise ValidationError("请输入正确的手机号码")
        return phone

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email == '' or email == 'null' or email is None:
            return ''
        pattern = re.compile(r"^([a-z0-9_.-]+)@([\da-z.-]+)\.([a-z.]{2,6})$")
        if not pattern.match(email):
            raise ValidationError("请输入合法的邮箱地址")
        return email
