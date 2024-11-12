from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Importing Library to ensure it's included

# Function-based view to list all books in the database
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library, listing all books available in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding all books related to this library to the context
        context['books'] = self.object.books.all()
        return context
