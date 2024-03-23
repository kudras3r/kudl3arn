from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """ User information """
    image = models.ImageField(default='user_image.jpg', upload_to='users_images', null=True, blank=True)
    tg_link = models.CharField(max_length=256, null=True, blank=True)
    vk_link = models.CharField(max_length=256, null=True, blank=True)
    git_link = models.CharField(max_length=2000, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}_profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    @property
    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            print(settings.MEDIA_URL)
            return settings.MEDIA_URL + 'user_image.jpg'


class Follower(models.Model):
    """ Follower model """
    user = models.CharField(max_length=150)

    user_followed = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} is followed to -> {self.user_followed}'
