from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token, name='obtain-token'),
    # other URL patterns
]

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router URLs for CRUD operations on books
    path('', include(router.urls)),  # This includes all CRUD routes automatically
]


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

