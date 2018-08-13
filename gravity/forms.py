from django import forms

from .import models

class AddGravityReading(forms.ModelForm):
    class Meta:
        model = models.SGravity
        fields = ['recipe','specific_gravity']
