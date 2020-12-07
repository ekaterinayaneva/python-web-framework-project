from django.contrib import admin

from app.models import Recipe, Rating, Comment


admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Comment)
