from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views import generic as views

from app.forms import CommentForm, RecipeForm
from app.models import Recipe, Comment, SaveRecipe
from core.clean_up import clean_up_files
from decorators import group_required



class HomePageView(views.TemplateView):
    template_name = 'home_page.html'


class RecipesView(views.ListView):
    template_name = 'recipes/recipes.html'
    model = Recipe
    context_object_name = 'recipes'


@method_decorator(group_required(groups=['User']), name='dispatch')
class RecipeDetailsView(views.DetailView):
    template_name = 'recipes/recipe_details.html'
    model = Recipe
    context_object_name = 'recipe'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context[self.context_object_name]
        context['form'] = CommentForm()
        context['ingredients_list'] = recipe.ingredients.split(', ')
        context['methods'] = recipe.method.split('.')
        context['can_save'] = self.request.user != recipe.user.user
        context['has_saved'] = recipe.saverecipe_set.filter(user_id=self.request.user.userprofile.id).exists()
        context['comments'] = list(recipe.comment_set.all())
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['comment'])
            comment.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
            comment.user = request.user.userprofile
            comment.save()
            return redirect('recipe details', pk=self.kwargs['pk'])


class UserSaveRecipeView(views.View):
    def get(self, request, **kwargs):
        user_profile = request.user.userprofile
        recipe = Recipe.objects.get(pk=kwargs['pk'])

        save_recipe = recipe.saverecipe_set.filter(user_id=user_profile.id).first()
        if save_recipe:
            save_recipe.delete()
        else:
            save_recipe = SaveRecipe(
                user=user_profile,
                recipe=recipe,
            )
            save_recipe.save()

        return redirect('recipe details', recipe.id)


class UpdateRecipeView(views.UpdateView):
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        url = reverse_lazy('recipe details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        old_image = self.get_object().image
        if old_image:
            clean_up_files(old_image.path)
        return super().form_valid(form)


class DeleteRecipeView(views.DeleteView):
    template_name = 'recipes/delete_recipe.html'
    model = Recipe
    success_url = reverse_lazy('current user profile')


@method_decorator(group_required(groups=['User']), name='dispatch')
class CreateRecipeView(views.CreateView):
    template_name = 'recipes/create_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.user = self.request.user.userprofile
        recipe.save()
        return redirect('recipe details', recipe.id)

