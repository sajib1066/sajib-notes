from django import forms
from .models import NewsLetter

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }