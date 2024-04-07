from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.contrib import auth, messages
from django.urls import reverse

from roadmaps.models import RoadMap
from users.forms import UserLoginForm, UserRegistrationForm, UpdateUserForm, UpdateProfileForm


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'kudl3arn',
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


def logout(request: HttpRequest) -> HttpResponseRedirect:
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:index'))


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
        'is_authorized': False
    }

    return render(request, 'users/auth/registration.html', context)


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    user_roadmaps = RoadMap.objects.filter(user=request.user)
    context = {
        'title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form,
        'user_roadmaps': user_roadmaps,
    }

    return render(request, 'users/profile.html', context)
