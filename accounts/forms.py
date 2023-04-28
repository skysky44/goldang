from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(label='주소', required=False)
    password1 = forms.CharField(
        label=_("비밀번호"),
        label_suffix='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("비밀번호 확인"),
        label_suffix='',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("비밀번호를 한번 더 입력하세요"),
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'picture',
            'address',
            'password1',
            'password2',
        )


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(label=_("이름"), label_suffix='')
    last_name = forms.CharField(label=_("성"), label_suffix='')
    email = forms.EmailField(label=_("이메일"), label_suffix='')
    password = ReadOnlyPasswordHashField(
        label='',
        label_suffix='',
        help_text=_(
            '<a href="{}">비밀번호 변경하기</a>'
        ),
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'picture',
        )