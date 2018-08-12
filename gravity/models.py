from django.db import models


class Recipe(models.Model):
    """ some attributes of a beer recipe. """
    created_at = models.DateTimeField(auto_now_add=True)
    recipe_name = models.CharField(max_length=100)
    original_gravity = models.DecimalField(max_digits=4, decimal_places=3)


class SGravity(models.Model):
    """ A set of measured specific gravities for a recipe. """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    specific_gravity = models.DecimalField(max_digits=4, decimal_places=3)

    class Meta:
        verbose_name_plural = 'S Gravity'
