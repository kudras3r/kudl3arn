from django import forms

from roadmaps.models import RoadMap


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
