from django.shortcuts import render
from django.views.generic import ListView

from notes.models import Note

class HomePage(ListView):
    queryset = Note.objects.all()
    template_name = 'index.html'

