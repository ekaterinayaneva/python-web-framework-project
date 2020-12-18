from django.urls import path
from . import views
from .views import HomePageView, RecipesView, CreateRecipeView, RecipeDetailsView, UpdateRecipeView, DeleteRecipeView, \
    UserSaveRecipeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('recipes', RecipesView.as_view(), name='recipes'),
    path('recipe/create/', CreateRecipeView.as_view(), name='create recipe'),
    path('recipe/details/<int:pk>', RecipeDetailsView.as_view(), name='recipe details'),
    path('recipe/edit/<int:pk>/', UpdateRecipeView.as_view(), name='edit recipe'),
    path('recipe/delete/<int:pk>', DeleteRecipeView.as_view(), name='delete recipe'),
    path('save/<int:pk>', UserSaveRecipeView.as_view(), name='save recipe'),
]
