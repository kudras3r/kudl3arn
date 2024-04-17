from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from users.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
