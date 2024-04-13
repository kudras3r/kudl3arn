from django.contrib.auth.models import User
from django import forms
from roadmaps.models import RoadMap


class RoadMapChangeForm(forms.Form):
    name = forms.CharField(max_length=128)
    description = forms.CharField()
    status = forms.CharField()

    class Meta:
        model = RoadMap
        fields = ('name', 'description', 'status')


class UpdateRoadMapForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    description = forms.CharField()
    status = forms.CharField()

    class Meta:
        model = RoadMap
        fields = ('name', 'description', 'status')
