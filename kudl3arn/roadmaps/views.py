from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from roadmaps.models import RoadMap


@login_required
def user_roadmaps(request: HttpRequest, username) -> HttpResponse:
    user = request.user
    roadmaps = RoadMap.objects.filter(id=user.id)
    context = {
        'title': f'{username} RMs',
        'user_roadmaps': roadmaps,
    }
    return render(request, 'roadmaps/user_roadmaps.html', context)
