from django.shortcuts import render
from django.views.generic import ListView, DetailView
from contactforms.forms import ContactForm

from notes.models import Note
from account.models import Profile
from account.forms import NewsLetterForm

class HomePage(ListView):
    queryset = Note.objects.filter(is_delete=False)
    template_name = 'index.html'

def home_page(request):
    queryset = Note.objects.filter(is_delete=False)
    forms = NewsLetterForm()
    if request.method == 'POST':
        forms = NewsLetterForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'form': forms,
        'queryset': queryset
    }
    return render(request, 'index.html', context)

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
