"""
URL configuration for kudl3arn project.
"""
from django.contrib import admin
from django.urls import path

from users.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
