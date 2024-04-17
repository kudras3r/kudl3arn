from django.db import models

from users.models import User


class BaseTechUnit(models.Model):
    """
    Base abstract model to extends another technologies, topics etc.
    name and description are the basic fields for all techs.
    """
    name = models.CharField(max_length=128, )
    description = models.TextField(max_length=1024)
    created_timestamp = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)

    class Meta:
        abstract = True


class RoadMap(BaseTechUnit):
    """
    RoadMap model. User -< RM -< TECH -< TOPIC -< SOURCE
    Something like 'Python, OOP, Backend etc'.
    """
    progress = models.IntegerField(default=0)  # in rounded percents
    status = models.CharField(max_length=11)  # in progress | is done | will come

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}_RM'

    def get_url(self):
        return f'/users/{self.user.username}/roadmap/rm{self.id}/'


class Technology(BaseTechUnit):
    """
    Technology model >- RoadMap.
    Descript the techs like 'classes, encapsulation, http etc'.
    """
    progress = models.IntegerField()  # in rounded percents
    is_done = models.BooleanField()

    roadmap = models.ForeignKey(RoadMap, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.roadmap.name}_technology'


class Topic(BaseTechUnit):
    """
    Topic model >- Technology.
    Topic is small things that you need to learn for technology.
    For example 'abstract classes, private data/methods in cpp, headers in http etc'
    """
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.technology.name}_topic'


class Source(models.Model):
    """
    Source model >- Topic.
    Stores the links/files/articles about Topic.
    """
    link = models.CharField(max_length=512, blank=True, null=True)
    file = models.FileField(upload_to='sources_files', null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.topic.name}_source'
