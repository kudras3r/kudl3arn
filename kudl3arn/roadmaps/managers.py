from django.http import HttpResponseRedirect

from .models import RoadMap, Technology, Topic, Source
from roadmaps.forms import UpdateRoadMapForm, UpdateTechnologyForm


class RoadMapManager:
    """
    Take RoadMap.id.
    Helps to encapsulate main logic from implementation logic.
    To roadmap showing in templates we need data structure like:
    {
        Technology1: {
            Topic1: QuerySet[Source],
            Topic2: ...
        },
        Technology2: {
            ...
        }
    }
    get_techs(id: int) -> structure see above
    """
    def __init__(self, id: int):
        self.rm = RoadMap.objects.get(id=id)

    @staticmethod
    def _get_topics_for_tech(tech: Technology) -> dict[Topic, Source]:
        topics = Topic.objects.filter(technology=tech)
        data = {}
        for topic in topics:
            data.setdefault(topic, None)
            sources = Source.objects.filter(topic=topic)
            data[topic] = sources
        return data

    def get_techs(self) -> dict[Technology, dict[Topic, Source]]:
        techs = Technology.objects.filter(roadmap=self.rm)
        rm_data = {}
        for tech in techs:
            rm_data.setdefault(tech, None)
            rm_data[tech] = self._get_topics_for_tech(tech)
        return rm_data

    def update(self, data: dict) -> HttpResponseRedirect:
        """
        See views update_roadmap func.
        If user send POST req with data - updating RoadMap table
        """
        form = UpdateRoadMapForm(data, instance=self.rm)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.rm.get_self_url())

    def get_update_form(self) -> UpdateRoadMapForm:
        """
        See views.
        If user just watch at his roadmap with GET req - let give him form
        """
        form = UpdateRoadMapForm(instance=self.rm)
        return form
