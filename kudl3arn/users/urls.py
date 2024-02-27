"""
URL configuration for kudl3arn project.
"""
from django.contrib import admin
from django.urls import path

from views import index

urlpatterns = [
    path('', index, name='index'),
]
