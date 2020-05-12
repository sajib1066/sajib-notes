from django.contrib import admin
from .models import Category, Tag, Comment, Note

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Note)