from django.shortcuts import render
from django.views.generic import ListView, DetailView
from contactforms.forms import ContactForm

from notes.models import Note

class HomePage(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'index.html'

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    forms = ContactForm()
    context = {
        'forms': forms
    }
    return render(request, 'contact.html', context)
