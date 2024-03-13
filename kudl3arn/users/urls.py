"""
URL configuration for kudl3arn project.
"""
from django.contrib import admin
from django.urls import path

from users.views import index, login, registration, profile, profile_edit

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile_edit'),
   # path('profile/')
]
