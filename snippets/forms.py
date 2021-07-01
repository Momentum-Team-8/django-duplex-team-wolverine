from .models import Snippet, User
from django import forms

class SnippetForm(forms.ModelForm):
    
    class Meta:
        model = Snippet
        fields = ["title", "code", "language", "description", "tags"]

