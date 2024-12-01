# BookListView: Retrieves all books
# Supports optional filtering by publication year using query parameters

# BookDetailView: Retrieves a single book by ID

# BookCreateView: Allows authenticated users to add a new book
# Custom validation and logic can be added in `perform_create`

# BookUpdateView: Allows authenticated users to update an existing book

# BookDeleteView: Allows authenticated users to delete a book


from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    """
    API endpoint for retrieving a list of books.
    - Supports filtering by title, author name, and publication year.
    - Supports searching by title and author name.
    - Supports ordering by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Adding filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields for searching
    search_fields = ['title', 'author__name']

    # Fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict creation to authenticated users

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict updates to authenticated users

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict deletion to authenticated users

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to everyone
# Create your views here.
