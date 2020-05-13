from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Note

class NoteListView(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'notes/note.html'

class NoteDetailView(DetailView):
    queryset = Note.objects.all()
    template_name = 'notes/details.html'
