from django import forms
from .models import Snippet, User


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ["title", "code", "language", "description", "tags"]