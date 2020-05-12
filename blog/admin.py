from django.contrib import admin
from .models import Category, Tag, Comment, Notes

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Notes)