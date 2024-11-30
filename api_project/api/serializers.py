from rest_framework import serializers
from .models import Book  # Adjust import if needed

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model
