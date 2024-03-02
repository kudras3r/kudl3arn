"""
URL configuration for kudl3arn project.
"""
from django.contrib import admin
from django.urls import path

from users.views import index, login, registration

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
   # path('profile/')
]
