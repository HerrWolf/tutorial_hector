from django.shortcuts import render
from django.urls import reverse
from .models import Book

# Create your views here.


def books_view(request):

    books = Book.objects.all()

    context = {
        'title': 'Books',
        'entity': 'Books',
        'page_name': 'List of Books',
        'url_list': reverse('books-view'),
        'books': books,
    }

    return render(request, "books.html" , context)


def book_create_view(request):

    context = {
        'title': 'Create Book',
        'entity': 'Books',
        'page_name': 'Create a new Book',
        'url_list': reverse('books-view'),
    }

    return render(request, "create.html" , context)