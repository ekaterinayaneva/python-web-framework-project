from django.shortcuts import render, redirect

from app.forms import CommentForm, RecipeForm, RecipeFormReadOnly
from app.models import Recipe, Comment, Rating


def home_page(request):
    return render(request, 'home_page.html')


def recipes(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/recipes.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients_list = recipe.ingredients.split(', ')
    methods = recipe.method.split('.')

    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': CommentForm(),
            'ingredients_list': ingredients_list,
            'methods': methods,
        }
        return render(request, 'recipes/recipe_details.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['comment'])
            comment.recipe = recipe
            comment.user = request.user.userprofile
            comment.save()
            return redirect('recipe details', pk)

        context = {
            'recipe': recipe,
            'form': form
        }
        return render(request, 'recipes/recipe_details.html', context)


def recipe_rate(request, pk):
    rate = Rating.objects.filter(user_id=request.user.userprofile.id, recipe_id=pk).first()
    if rate:
        rate.delete()
    else:
        recipe = Recipe.objects.get(pk=pk)
        rate = Rating(test=str(pk), user=request.user.userprofile)
        rate.recipe = recipe
        rate.save()

    return redirect('recipe details', pk)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {
            'recipe': recipe,
            'form': form
        }
        return render(request, 'recipes/edit_recipe.html', context)

    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()

            return redirect('recipe details', pk)

        context = {
            'recipe': recipe,
            'form': form
        }
        return render(request, 'recipes/edit_recipe.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients_list = recipe.ingredients.split(', ')
    methods = recipe.method.split('.')

    if request.method == 'GET':
        context = {'recipe': recipe,
                   'ingredients_list': ingredients_list,
                   'methods': methods,
        }
        return render(request, 'recipes/delete_recipe_sure.html', context)

    else:
        recipe.delete()
        return redirect('current user profile')


def create_recipe(request):

    if request.method == 'GET':
        form = RecipeForm()
        context = {'form': form}
        return render(request, 'recipes/create_recipe.html', context)

    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('recipes')

        context = {'form': form}
        return render(request, 'recipes/create_recipe.html', context)



