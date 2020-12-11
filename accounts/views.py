from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm, ProfileForm
from accounts.models import UserProfile


def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm()
        }
        return render(request, 'accounts/register_user.html', context)

    else:
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user
            )
            profile.save()

            login(request, user)
            return redirect('home page')

        context = {
            'form': form,
        }
        return render(request, 'accounts/register_user.html', context)


@login_required
def logout_user(req):
    logout(req)
    return redirect('home page')


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'recipes': user.userprofile.recipe_set.all(),
            'saved_recipes': user.userprofile.saverecipe_set.all(),
            'form': ProfileForm(),
        }

        return render(request, 'accounts/user_profile.html', context)

    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')
