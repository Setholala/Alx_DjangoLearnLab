from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy()
    template_name ='relationship_app/register.html'

