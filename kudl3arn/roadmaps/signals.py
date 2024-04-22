from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


@receiver(post_save, sender=User)
def save_roadmap(sender, instance, **kwargs):
    try:
        instance.roadmap.save()
    except AttributeError:
        ...
