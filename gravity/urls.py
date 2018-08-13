from django.urls import path
from . import views

app_name = 'gravity'

urlpatterns = [
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('<recipe_pk>', views.gravity, name='gravity'),
]
