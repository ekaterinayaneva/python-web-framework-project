from django.contrib import admin

from app.models import Recipe, SaveRecipe, Comment


admin.site.register(Recipe)
admin.site.register(SaveRecipe)
admin.site.register(Comment)
