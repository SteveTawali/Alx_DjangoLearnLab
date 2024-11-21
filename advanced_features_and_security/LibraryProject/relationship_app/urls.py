# URL configuration for LibraryProject project.

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
from .views import admin_view, librarian_view, member_view, list_books

urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Authentication Views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-Based Access Views
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),

    # Book Management Views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
