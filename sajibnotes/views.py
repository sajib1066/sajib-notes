from django.shortcuts import render
from django.views.generic import ListView

from notes.models import Note

class HomePage(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'index.html'

