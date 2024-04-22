from django import forms

from roadmaps.models import RoadMap, Technology


class UpdateRoadMapForm(forms.ModelForm):
    """
    Updates basic info about RM
    """
    name = forms.CharField(max_length=128)
    description = forms.CharField()
    status = forms.CharField()

    class Meta:
        model = RoadMap
        fields = ('name', 'description', 'status')


class UpdateTechnologyForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    description = forms.CharField()
    is_done = forms.BooleanField(required=False)

    class Meta:
        model = Technology
        fields = ('name', 'description', 'is_done')


class UpdateTopicForm(forms.ModelForm):
    ...


class UpdateSourceForm(forms.ModelForm):
    ...
