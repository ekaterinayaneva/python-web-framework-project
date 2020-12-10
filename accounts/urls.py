from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import logout_user, register_user #user_profile

urlpatterns = [
    path('register/', register_user, name='register user'),
    path('login/', LoginView.as_view(template_name='accounts/login_user.html'), name='login user', ),
#    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
 #   path('profile/', user_profile, name='current user profile'),
  #  path('profile/<int:pk>', user_profile, name='user profile'),
]
