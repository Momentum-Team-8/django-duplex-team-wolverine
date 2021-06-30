from django import forms
from .models import Snippet, User


class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.TextInput()

    class Meta:
        model = Snippet
        fields = ["title", "code", "language", "description", "tags"]
