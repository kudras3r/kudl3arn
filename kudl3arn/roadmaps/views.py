from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from roadmaps.models import RoadMap
from roadmaps.forms import UpdateRoadMapForm


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
        # 'is_authorized': True,
        'user_roadmap': roadmap,
    }
    return render(request, 'roadmaps/user_roadmap.html', context)


@login_required
def update_roadmap(request: HttpRequest, username: str, rm_id: int) -> HttpResponse:
    roadmap = RoadMap.objects.get(id=rm_id)
    if request.method == 'POST':
        form = UpdateRoadMapForm(request.POST, instance=roadmap)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/users/{request.user.username}/roadmap/rm{roadmap.id}/')
    else:
        form = UpdateRoadMapForm(instance=roadmap)
    # roadmap = RoadMap.objects.get(id=rm_id)
    context = {
        'title': 'RM update',
        'rm_form': form,
        'roadmap': roadmap,
    }

    return render(request, 'roadmaps/update_roadmap.html', context)

