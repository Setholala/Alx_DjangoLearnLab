from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_book(request):
    books= Book.objects.all()
    render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetail(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library
