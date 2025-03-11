from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .models import Book
from .models import Library
from .utils import role_required

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    render(request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    template_name = 'relationship_app/library_detail.html'
    model = Library

def custom_login_view(request):
    error_message = None

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
        
    return render(request, 'relationship_app/login.html', {'error_message' : error_message})

        
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@role_required('Admin')
def admin_view(request):
    return render(request, 'admin_dashboard.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'librarian_dashboard.html')
@role_required ('Member')
def member_view(request):
    return render(request, 'member_dashboard.html')
