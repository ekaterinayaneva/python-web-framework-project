from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm
from accounts.models import UserProfile


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm()
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



# def login_user(req):
#     if req.method == 'GET':
#         context = {
#             'login_form': LoginForm(),
#             }
#
#         return render(req, 'accounts/login_user.html', context)
#
#     else:
#         login_form = LoginForm(req.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(req, user)
#                 return redirect('home page')
#
#
#             context = {
#                 'login_form': login_form,
#             }
#             return render(req, 'accounts/login_user.html', context)


@login_required
def logout_user(req):
    logout(req)
    return redirect('home page')

