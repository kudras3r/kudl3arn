from django.apps import AppConfig


class RoadmapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'roadmaps'

    def ready(self):
        import roadmaps.signals
