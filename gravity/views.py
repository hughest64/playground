from django.shortcuts import render

def gravity(request):
    s_gravity = '1.050'
    # add form here
    return render(request, 'gravity/gravity_form.html', {'s_gravity':s_gravity})
