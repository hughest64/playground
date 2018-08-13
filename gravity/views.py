from django.shortcuts import render

from . import forms, models

def recipe_list(request):
    recipes = models.Recipe.objects.all()
    return render(request, 'gravity/recipe_list.html', {'recipes':recipes})

def gravity(request, recipe_pk):
    form = forms.AddGravityReading(initial={'recipe':recipe_pk})
    print(form.fields['recipe'].label) #= recipe_pk
    recipe = models.Recipe.objects.get(id=recipe_pk)
    context = {'form':form, 'recipe':recipe,}

    if request.method == 'POST':
        form = forms.AddGravityReading(request.POST, )
        if form.is_valid():
            form.save()
            return render(request, 'gravity/gravity_form.html', context)
    return render(request, 'gravity/gravity_form.html', context)
