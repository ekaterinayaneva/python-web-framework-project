from django.urls import path
from . import views
from .views import home_page, recipes, create_recipe, recipe_details, edit_recipe, delete_recipe

urlpatterns = [
    path('', home_page, name='home page'),
    path('recipes', recipes, name='recipes'),
    path('recipe/create/', create_recipe, name='create recipe'),
    path('recipe/details/<int:pk>', recipe_details, name='recipe details'),
    path('recipe/edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('recipe/delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('recipe/delete/<int:pk>', delete_recipe, name='delete recipe sure'),

]
