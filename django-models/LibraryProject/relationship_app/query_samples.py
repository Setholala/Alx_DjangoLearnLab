from relationship_app.models import Book, Author, Librarian, Library

author = Author.objects.get(name=author_name)
for book in author.books.all().values():
    print(book)

books = Book.objects.filter(author=author)
print(books)

library = Library.objects.get(name=library_name)

librarian = Librarian.objects.get(name=
print(librarian.library.name)
