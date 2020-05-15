from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Note, Comment
from .forms import CommentForm

class NoteListView(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'notes/note.html'

class NoteDetailView(DetailView):
    queryset = Note.objects.all()
    template_name = 'notes/details.html'

def note_details(request, slug):
    note = Note.objects.get(slug=slug)
    comment = Comment.objects.filter(note=note)
    form = CommentForm(request.POST or None)
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    website = request.POST.get('website')
    message = request.POST.get('message')
    if (email):
        Comment.objects.create(note=note, name=name, email=email, website=website, message=message)
        context = {
            'form': form
        }
        return render(request, 'notes/details.html', context)
    
    context = {
        'note': note,
        'comment': comment,
        'form': form
    }
    return render(request, 'notes/details.html', context)
