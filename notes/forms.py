from django import forms
from django.core.exceptions import ValidationError

from .models import Note


class NotesCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'description')
        labels = {
            "title": "",
            "description": "",
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'id': 'editorx'})
        }
