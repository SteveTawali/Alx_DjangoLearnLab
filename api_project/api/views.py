from django.shortcuts import render
from rest_framework import generics
from .models import Book  # Ensure the Book model is imported
from .serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
