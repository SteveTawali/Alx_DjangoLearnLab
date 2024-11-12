from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    list_filter = ('author', 'title', 'publication_year')
    search_fields = ('author', 'title', 'publication_year')
    