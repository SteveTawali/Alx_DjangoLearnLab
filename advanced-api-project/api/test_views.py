from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.test import TestCase
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')  # Log in the user

        # Create a test book instance
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2024
        )
    
    def test_create_book(self):
        response = self.client.post('/api/books/create/', {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2025
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2022,
            author=self.author
        )
        self.client = APIClient()

    def test_create_book(self):
        data = {
            'title': "New Test Book",
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Test Book")

    def test_update_book(self):
        data = {
            'title': "Updated Test Book"
        }
        response = self.client.put(f'/api/books/{self.book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Test Book")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure at least one book is listed
