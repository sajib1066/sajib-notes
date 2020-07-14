from django.contrib import admin
from .models import Profile, NewsLetter

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'title', 'date']
    search_fields = ['name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(NewsLetter)