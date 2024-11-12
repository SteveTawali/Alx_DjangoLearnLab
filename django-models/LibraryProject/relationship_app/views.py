from django.shortcuts import render
from .models import Book, Library

# Function-based view to list all books in the database
def list_books(request):
    books = Book.objects.all()  # Using Book.objects.all() to fetch all book records
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Create your views here.
