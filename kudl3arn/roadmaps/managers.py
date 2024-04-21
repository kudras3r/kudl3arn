from .models import RoadMap, Technology, Topic, Source


class RoadMapManager:
    def __init__(self, id: int):
        self.rm = RoadMap.objects.get(id=id)

    def get_techs(self) -> dict[Technology, dict[Topic, Source]]:
        techs = Technology.objects.filter(roadmap=self.rm)
        rm_data = {}
        for tech in techs:
            rm_data.setdefault(tech, None)
            rm_data[tech] = self._get_topics_for_tech(tech)
        return rm_data

    @staticmethod
    def _get_topics_for_tech(tech: Technology) -> dict[Topic, Source]:
        topics = Topic.objects.filter(technology=tech)
        data = {}
        for topic in topics:
            data.setdefault(topic, None)
            sources = Source.objects.filter(topic=topic)
            data[topic] = sources
        return data
