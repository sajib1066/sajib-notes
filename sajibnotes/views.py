from django.shortcuts import render
from django.views.generic import ListView, DetailView
from contactforms.forms import ContactForm

from notes.models import Note
from account.models import Profile

class HomePage(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'index.html'

def about_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
        context = {'profile': profile}
        return render(request, 'about.html', context)
    except:
        return render(request, 'about.html')

def contact_page(request):
    forms = ContactForm()
    try:
        profile = Profile.objects.get(user=request.user)
        context = {
            'forms': forms,
            'profile': profile
        }
        return render(request, 'contact.html', context)
    except:
        context = {
            'forms': forms
        }
        return render(request, 'contact.html', context)
