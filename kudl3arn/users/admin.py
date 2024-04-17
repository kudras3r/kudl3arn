from django.contrib import admin

from users.models import Follower, Profile


admin.site.register(Profile)
admin.site.register(Follower)
