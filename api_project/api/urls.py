from django.urls import path
from .views import BookList
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),  # Route to the api app's URLs
]


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

