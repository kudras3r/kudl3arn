from django.contrib import admin

from users.models import Follower, Profile #User


# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Follower)
