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

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.strip():
            raise forms.ValidationError("Name cannot be empty.")
        return name
