from django.shortcuts import render

from . import forms, models

def recipe_list(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'gravity/recipe_list.html', {'recipes':recipes})

def gravity(request):
    s_gravity = '1.050'
    form = forms.AddGravityReading()
    # add form here
    return render(request, 'gravity/gravity_form.html', {'s_gravity':s_gravity})
