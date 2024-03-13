from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'kudl3arn',
        'authorized': False
    }
    return render(request, 'users/index.html', context)


def login(request: HttpRequest) -> HttpResponseRedirect:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'title': 'Login',
        'authorized': True
    }
    return render(request, 'users/auth/login.html', context)


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Registrate',
        'authorized': False
    }
    return render(request, 'users/auth/registration.html', context)


def profile(request) -> HttpResponse:
    context = {
        'title': 'Profile',
        'username': request.user.username,
        'tg_link': request.user.tg,
        'vk_link': request.user.vk,
        'git_link': request.user.github
    }
    return render(request, 'users/profile.html', context)


def profile_edit(request) -> HttpResponse:
    if request.method == 'POST':
        queryset = User.objects.get(pk=request.user.id)
        form = UserProfileForm(data=request.POST, instance=queryset) #instance=request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Edit your profile',
        'form': form
    }
    return render(request, 'users/profile_edit.html', context)



