from django.shortcuts import render
from .models import Book, Library

# Function-based view to list all books in the database
def list_books(request):
    books = Book.objects.all()  # Using Book.objects.all() to fetch all book records
    return render(request, 'relationship_app/list_books.html', {'books': books})


cfrom django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Importing Library along with Book

# Function-based view to list all books in the database
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Importing Library along with Book

# Function-based view to list all books in the database
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Create your views here.
