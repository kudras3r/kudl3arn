from django.urls import path
from roadmaps.views import user_roadmaps

app_name = 'roadmaps'

urlpatterns = [
    path('user_roadmaps/', user_roadmaps, name='user_roadmaps'),
]
