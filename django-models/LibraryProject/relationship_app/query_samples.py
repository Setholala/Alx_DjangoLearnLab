from relationship_app.models import Book, Author, Librarian, Library

author = Author.objects.get(name='JohnDoe')
for book in author.books.all().values():
    print(book)

books = Book.objects.all()
print(books)

library = Library.objects.get(name=library_name)
print(library.librarian.name)
