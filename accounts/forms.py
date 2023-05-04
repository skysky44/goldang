from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, AuthenticationForm,  PasswordResetForm
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from django.forms import CharField, PasswordInput
from django.core.validators import RegexValidator


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
            'nickname',
            'email',
            'picture',
            'address',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = '아이디'
        self.fields['nickname'].label = '닉네임'
        self.fields['email'].label = '이메일'
        self.fields['picture'].label = '프로필 사진'
        self.fields['address'].label = '주소'

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '아이디',
            'aria-label': 'Username',
            'aria-describedby': 'username-addon'
        })
        self.fields['nickname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '닉네임',
            'aria-label': 'Nickname',
            'aria-describedby': 'nickname-addon'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '이메일',
            'aria-label': 'Email',
            'aria-describedby': 'email-addon'
        })
        self.fields['picture'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '프로필 사진',
            'aria-label': 'Picture',
            'aria-describedby': 'picture-addon'
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '주소',
            'aria-label': 'Address',
            'aria-describedby': 'address-addon'
        })


class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(label='주소', required=False)
    nickname = forms.CharField(label='닉네임', max_length=30,
                               validators=[RegexValidator(r'^[\w.@+-]+$', _('닉네임은 30자 이내의 알파벳, 숫자, 밑줄, @, ., +, - 문자만 가능합니다.'))])
    picture = forms.ImageField(label='프로필 사진', required=False,
                                help_text='2MB 이하의 jpg, jpeg, png, gif 이미지 파일을 업로드해주세요.')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'nickname',
            'email',
            'picture',
            'address',
            'password1',
            'password2',
        )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("이메일 주소"),
        label_suffix='',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
            'placeholder': '이메일 주소'
        }),
        help_text=_("암호 재설정 링크를 받을 이메일 주소를 입력하세요."),
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
            'nickname',
            'email',
            'picture',
            
        )

# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(label='아이디',
#                                widget = forms.TextInput(attrs=
#                                                         class="form-control",
#                                                           placeholder="아이디",
#                                                             aria-label="Username" aria' 
#     )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '아이디',
            'aria-label': 'Username',
            'aria-describedby': 'username-addon'
        })
        self.fields['password'].label = '비밀번호'
        self.fields['password'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '비밀번호',
            'aria-label': 'Password',
            'aria-describedby': 'password-addon'
        })