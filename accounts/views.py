from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import JsonResponse

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('plates:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('plates:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('plates:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('plates:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('plates:index')


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('plates:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plates:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('plates:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def profile(request, username):
    User = get_user_model()
    context = {
        'person': User.objects.get(username=username),
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    me = request.user
    if me != user:
        if me in user.followers.all():
            # follow 취소
            user.followers.remove(me)
            is_followed = False
        else:
            # follow
            user.followers.add(me)
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followings_count': user.followings.count(),
            'followers_count': user.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', user.username)
