from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy


from accounts.forms import RegisterForm, ProfileForm
from accounts.models import UserProfile

from django.views import generic as views



class RegisterUserView(views.CreateView):
    template_name = 'accounts/register_user.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm
        return context

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user
            )
            profile.save()

            login(request, user)

            group = Group.objects.get(name='User')
            user.groups.add(group)
            return redirect('home page')


class LogOutView(LogoutView):
    next_page = reverse_lazy('home page')



# def user_profile(request, pk=None):
#     user = request.user if pk is None else User.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'profile_user': user,
#             'profile': user.userprofile,
#             'recipes': user.userprofile.recipe_set.all(),
#             'saved_recipes': user.userprofile.saverecipe_set.all(),
#             'form': ProfileForm(),
#         }
#
#         return render(request, 'accounts/user_profile.html', context)
#
#     else:
#         form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('current user profile')
#
#         return redirect('current user profile')



class UserProfileView(views.UpdateView):
    template_name = 'accounts/user_profile.html'
    form_class = ProfileForm
    model = UserProfile
    success_url = reverse_lazy('current user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user \
            if pk is None \
            else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_user'] = self.get_object().user
        context['profile'] = self.get_object().user.userprofile
        context['recipes'] = self.get_object().recipe_set.all()
        context['saved_recipes'] = self.get_object().saverecipe_set.all()
        context['form'] = ProfileForm()

        return context
