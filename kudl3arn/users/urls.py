from django.urls import path, include

from users.views import index, login, logout, registration, profile

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('', include('roadmaps.urls')),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
]
