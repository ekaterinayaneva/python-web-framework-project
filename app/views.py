from django.shortcuts import render, redirect

from app.forms import CommentForm, RecipeForm, RecipeFormReadOnly
from app.models import Recipe, Rating


def home_page(request):
    return render(request, 'home_page.html')


def recipes(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/recipes.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        'recipe': recipe,
               }
    return render(request, 'recipes/recipe_details.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {'recipe': recipe,
                   'form': form
                   }
        return render(request, 'recipes/edit_recipe.html', context)

    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe details', pk)

        context = {'recipe': recipe,
                   'form': form
                   }
        return render(request, 'recipes/edit_recipe.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeFormReadOnly(instance=recipe)
        context = {'recipe': recipe,
                   'form': form
                   }
        return render(request, 'recipes/delete_recipe.html', context)

    else:
        recipe.delete()
        return redirect('home page')


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'recipes/create_recipe.html', context)

    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')

        context = {'form': form}
        return render(request, 'recipes/create_recipe.html', context)


def recipe_rate(request, pk):
    recipe = Recipe.objects.get(pk= pk)
    rate = Rating(test=str(pk))
    rate.recipe = recipe
    rate.save()
    return redirect('recipe details', pk)
