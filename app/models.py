from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='recipes')
    description = models.TextField()
    method = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField()


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
