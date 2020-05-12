from django.db import models
from django.contrib.auth.models import User

from sajibnotes.helper import get_current_user

class Profile(models.Model):
    current_user = get_current_user
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=current_user)
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='profile/')
    title = models.CharField(max_length=240)
    about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
