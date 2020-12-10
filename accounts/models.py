from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='profiles/', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.user.username};'

