from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import CommentForm, RecipeForm
from app.models import Recipe, Comment, SaveRecipe



def home_page(request):
    return render(request, 'home_page.html')


def recipes(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'recipes/recipes.html', context)


@login_required
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
            'has_saved': recipe.saverecipe_set.filter(user_id=request.user.userprofile.id).exists(),
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
            'form': form,
            'ingredients_list': ingredients_list,
            'methods': methods,
            'has_saved': recipe.saverecipe_set.filter(user_id=request.user.userprofile.id).exists(),
        }
        return render(request, 'recipes/recipe_details.html', context)


def user_save_recipe(request, pk):
    save_recipe = SaveRecipe.objects.filter(user_id=request.user.userprofile.id, recipe_id=pk).first()
    if save_recipe:
        save_recipe.delete()
    else:
        recipe = Recipe.objects.get(pk=pk)
        save_recipe = SaveRecipe(test=str(pk), user=request.user.userprofile)
        save_recipe.recipe = recipe
        save_recipe.save()

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

    if request.method == 'GET':
        context = {'recipe': recipe}
        return render(request, 'recipes/delete_recipe.html', context)

    else:
        recipe.delete()
        return redirect('home page')


@login_required
def create_recipe(request):

    if request.method == 'GET':
        form = RecipeForm()
        context = {'form': form}
        return render(request, 'recipes/create_recipe.html', context)

    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user.userprofile
            form.save()
            return redirect('recipes')

        context = {'form': form}
        return render(request, 'recipes/create_recipe.html', context)



