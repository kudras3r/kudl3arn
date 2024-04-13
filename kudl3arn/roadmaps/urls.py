from django.urls import path
from roadmaps.views import user_roadmaps, user_roadmap, update_roadmap

app_name = 'roadmaps'

urlpatterns = [
    path('<str:username>/roadmap/rm<int:rm_id>/update/', update_roadmap, name='update_roadmap'),
    path('<str:username>/roadmap/rm<int:rm_id>/', user_roadmap, name='user_roadmap'),
    path('<str:username>/user_roadmaps/', user_roadmaps, name='user_roadmaps'),
    # path('<str:username>/user_roadmaps/rm<int:rm_id>', user_roadmap, name='user_roadmap'),
    # path('user_roadmaps/<int:rm_id>/', user_roadmap, name='user_roadmap'),
]
