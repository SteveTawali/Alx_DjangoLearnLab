 # CRUD Operations Documentation

## Create Operation

**Command:**
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)


retrieved_book.delete()
all_books = Book.objects.all()
print(all_books)

