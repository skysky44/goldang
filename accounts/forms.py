from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "아이디를 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )
    email = forms.EmailField(
        label="이메일",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "이메일을 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )

    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "비밀번호를 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "비밀번호를 다시 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )

    picture = forms.ImageField(
        label="사진",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "placeholder": "사진을 선택하세요",
                "style": "width: 400px;",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "picture", "password1", "password2")


# class CustomPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(
#         label=_("이메일 주소"),
#         label_suffix="",
#         max_length=254,
#         widget=forms.EmailInput(
#             attrs={
#                 "autocomplete": "email",
#                 "class": "form-control",
#                 "placeholder": "이메일 주소",
#             }
#         ),
#         help_text=_("암호 재설정 링크를 받을 이메일 주소를 입력하세요."),
#     )


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        label="이메일",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "이메일을 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )
    nickname = forms.CharField(
        label="닉네임",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "닉네임을 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )
    picture = forms.ImageField(
        label="사진",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "placeholder": "사진을 선택하세요",
                "style": "width: 400px;",
            }
        ),
    )
    address = forms.CharField(
        label="주소",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "주소를 입력하세요",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )

    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("email", "nickname")


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "아이디를 입력하세요",
                "style": "width: 400px; height: 50px;",
                "autocomplete": "username",
                #'style' : 'width: 400px;'
            }
        ),
    )
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "비밀번호를 입력하세요",
                "style": "width: 400px; height: 50px;",
                "autocomplete": "current-password",
                #'style' : 'width: 400px;'
            }
        ),
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "기존 비밀번호",
                "style": "width: 400px; height: 50px;",
            }
        ),
    )
    new_password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "새 비밀번호",
                "style": "width: 400px; height: 50px;",
            }
        ),
        help_text="",
    )
    new_password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "새 비밀번호 확인",
                "style": "width: 400px; height: 50px;",
            }
        ),
        help_text="",
    )
