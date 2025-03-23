from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'articles/list.html', {'books': books})

@permission_required('yourapp.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Book.objects.create(title=title, content=content, author=request.user)
        return redirect('book_list')
    return render(request, 'books/create.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    article = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('book_list')
    return render(request, 'books/edit.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Article, pk=pk)
    book.delete()
    return redirect('book_list')
