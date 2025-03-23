from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Ensure 'Book' model exists in models.py
        fields = ['title', 'author', 'description']  # Adjust fields as needed

    # Additional validation example
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.strip():
            raise forms.ValidationError("Title cannot be empty.")
        return title
