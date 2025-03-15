from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .models import Book
from .models import Library
from .utils import role_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
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

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book_list')

    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.published_date = request.POST.get('published_date', book.published_date)
        book.save()
        return redirect('book_list')

    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request, 'relationship_app/delete_book.html', {'book': book})
