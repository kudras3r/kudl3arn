from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User information.
    Profile <-> User
    """
    image = models.ImageField(
        default='user_image.jpg', upload_to='users_images',
        null=True, blank=True
    )
    tg_link = models.CharField(max_length=256, null=True, blank=True)
    vk_link = models.CharField(max_length=256, null=True, blank=True)
    git_link = models.CharField(max_length=2048, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}_profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def get_image(self):
        """ Helps Django-templates find avatar img path """
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return settings.MEDIA_URL + 'user_image.jpg'


class Follower(models.Model):
    """ Follower model """
    user = models.CharField(max_length=150)

    user_followed = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} is followed to -> {self.user_followed}'
