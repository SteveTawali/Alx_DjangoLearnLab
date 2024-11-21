from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Replace this with your logic to fetch and display books
    return render(request, 'bookshelf/book_list.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def books(request):
    # Replace this with your logic to fetch a specific book or handle books
    return HttpResponse("Books endpoint")
