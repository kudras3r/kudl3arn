from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/index.html')


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/auth/login.html')


def registration(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/auth/registration.html')

