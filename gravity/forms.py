from django import forms

from .import models

class AddGravityReading(forms.Form):
    gravity_form = forms.IntegerField()
