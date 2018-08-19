from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from . import forms, models

def recipe_list(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'gravity/recipe_list.html', {'recipes':recipes})

@csrf_exempt
@login_required
def gravity(request, recipe_pk):
    form = forms.AddGravityReading(initial={'recipe':recipe_pk})
    recipe = models.Recipe.objects.get(id=recipe_pk)
    context = {'form':form, 'recipe':recipe,}

    if request.method == 'POST':
        form = forms.AddGravityReading(request.POST, )
        if form.is_valid():
            form.save()
            return render(request, 'gravity/gravity_form.html', context)
        else:
            print('The form is not valid')
            return render(request, 'gravity/gravity_form.html', context)
    return render(request, 'gravity/gravity_form.html', context)


def gravity_main(request):
    "The main gravity page, currently does nothing"
    return render(request, 'gravity/gravity_login.html')
