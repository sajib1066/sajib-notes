from django.shortcuts import render
from django.views.generic import (
    DetailView
)
from .models import Note

class NoteDetailView(DetailView):
    queryset = Note.objects.all()
    template_name = 'notes/details.html'
