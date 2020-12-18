from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import RegisterUserView, LogOutView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginView.as_view(template_name='accounts/login_user.html'), name='login user'),
    path('logout/', LogOutView.as_view(), name='logout user'),
    path('profile/', UserProfileView.as_view(), name='current user profile'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='user profile'),
]
