from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from roadmaps.forms import UpdateRoadMapForm, UpdateTechnologyForm
from roadmaps.models import RoadMap, Technology
from roadmaps.managers import RoadMapManager


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
    manager = RoadMapManager(rm_id)
    roadmap = manager.rm
    rm_data = manager.get_techs()
    context = {
        'title': roadmap.name,
        'user_roadmap': roadmap,
        'rm_data': rm_data,
    }
    return render(request, 'roadmaps/user_roadmap.html', context)


@login_required
def update_roadmap(request: HttpRequest, username: str, rm_id: int) -> HttpResponse:
    roadmap = RoadMap.objects.get(id=rm_id)
    if request.method == 'POST':
        form = UpdateRoadMapForm(request.POST, instance=roadmap)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(roadmap.get_self_url())
    else:
        rm_form = UpdateRoadMapForm(instance=roadmap)

    context = {
        'title': 'RM update',
        'rm_form': rm_form,
        'roadmap': roadmap,
    }
    return render(request, 'roadmaps/update_roadmap.html', context)


@login_required()
def update_tech(request, username: str, rm_id: int, tech_id: int):
    tech = Technology.objects.get(id=tech_id)
    if request.method == 'POST':
        tech_form = UpdateTechnologyForm(request.POST, instance=tech)
        if tech_form.is_valid():
            tech_form.save()
            return HttpResponseRedirect(tech.roadmap.get_self_url())
    else:
        tech_form = UpdateTechnologyForm(instance=tech)
    context = {
        'title': 'Tech Update',
        'tech_form': tech_form,
        'tech': tech,
        'rm_id': rm_id,
    }
    return render(request, 'roadmaps/update_tech.html', context)
