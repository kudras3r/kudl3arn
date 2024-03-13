from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    """ Custom User model """
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    github = models.CharField(max_length=2000, null=True, blank=True)
    tg = models.CharField(max_length=256, null=True, blank=True)
    vk = models.CharField(max_length=256, null=True, blank=True)
    sex = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.username}'


# class UserProfile(models.Model):
#     """ User information """
#     about = models.TextField(max_length=500, null=True, blank=True)
#     github = models.CharField(max_length=2000, null=True, blank=True)
#     tg = models.CharField(max_length=256, null=True, blank=True)
#     vk = models.CharField(max_length=256, null=True, blank=True)
#     sex = models.BooleanField(null=True, blank=True)
#
#     user = models.ForeignKey(to='User', on_delete=models.PROTECT)


class Follower(models.Model):
    """ Follower model """
    user = models.CharField(max_length=150)

    user_followed = models.ForeignKey(to='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} is followed to -> {self.user_followed}'
