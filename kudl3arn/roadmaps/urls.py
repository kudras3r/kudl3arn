from django.urls import path

from roadmaps.views import (user_roadmaps, user_roadmap,
                            update_roadmap, update_tech)

app_name = 'roadmaps'

urlpatterns = [
    path('<str:username>/roadmap/rm<int:rm_id>/update_rm/', update_roadmap, name='update_roadmap'),
    path('<str:username>/roadmap/rm<int:rm_id>/update_tech/<int:tech_id>/', update_tech, name='update_tech'),
    path('<str:username>/roadmap/rm<int:rm_id>/', user_roadmap, name='user_roadmap'),
    path('<str:username>/user_roadmaps/', user_roadmaps, name='user_roadmaps'),
]
