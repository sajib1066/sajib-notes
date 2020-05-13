from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from account.models import Profile
from sajibnotes.helper import get_current_user

class Category(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=120, unique=True)
    video_url = models.URLField()
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    is_delete = models.BooleanField(default=False)
    current_user = get_current_user
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=current_user)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
