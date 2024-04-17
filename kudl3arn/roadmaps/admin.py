from django.contrib import admin

from .models import RoadMap, Technology, Topic, Source

admin.site.register(RoadMap)
admin.site.register(Topic)
admin.site.register(Technology)
admin.site.register(Source)
