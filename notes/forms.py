from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control", "type": 'email'}),
            'website': forms.TextInput(attrs={"class": "form-control", "type": "url"}),
            'message': forms.Textarea(attrs={"class": "form-control"}),
        }