"""
URL configuration for kudl3arn project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import index, login, registration, profile

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
