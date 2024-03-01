from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib import auth

from users.forms import UserLoginForm
from users.models import User

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/index.html')


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username, password)
            if user:
                auth.login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/auth/login.html', context)


def registration(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/auth/registration.html')

