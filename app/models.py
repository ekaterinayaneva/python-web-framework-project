from django.db import models

from accounts.models import UserProfile


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='recipes') #, blank=True, null=True ,'
    description = models.TextField()
    method = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField()

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.title}; {self.user.user.username}'



class SaveRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

