from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RoadMap
from users.models import User


# @receiver(post_save, sender=User)
# def create_roadmap(sender, instance, created, **kwargs):
#     if created:
#         RoadMap.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_roadmap(sender, instance, **kwargs):
    try:
        instance.roadmap.save()
    except AttributeError:
        ...
    