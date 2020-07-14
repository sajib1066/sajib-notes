from django.db import models
from django.contrib.auth.models import User

from sajibnotes.helper import get_current_user

class Profile(models.Model):
    current_user = get_current_user
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=current_user)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    address = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    title = models.CharField(max_length=240)
    about = models.TextField()
    phone_number = models.CharField(max_length=14, unique=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email