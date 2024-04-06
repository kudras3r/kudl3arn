from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from roadmaps.models import RoadMap


@login_required
def user_roadmaps(request: HttpRequest, username) -> HttpResponse:
    user = request.user
    roadmaps = RoadMap.objects.filter(user=user)
    context = {
        'title': f'{username} RMs',
        'user_roadmaps': roadmaps,
    }
    return render(request, 'roadmaps/user_roadmaps.html', context)


@login_required
def user_roadmap(request: HttpRequest, username: str, rm_id: int) -> HttpResponse:
    roadmap = RoadMap.objects.get(id=rm_id)
    context = {
        'title': roadmap.name,
        'is_authorized': True,
        'user_roadmap': roadmap,
    }
    return render(request, 'roadmaps/user_roadmap.html', context)

