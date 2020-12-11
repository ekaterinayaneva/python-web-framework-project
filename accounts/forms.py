from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    # def clean_email(self):
    #     email = self.cleaned_data.get('email', False)
    #     if not email:
    #         raise forms.ValidationError('Email is required')
    #     return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
  #      fields = '__all__'
        exclude = ('user', )
