from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Book
from .forms import BookForm
from faker import Faker


def books_view(request):
    books = Book.objects.order_by('-id')

    context = {
        'title': 'Books',
        'entity': 'Books',
        'page_name': 'List of Books',
        'url_list': reverse('books-view'),
        'books': books,
    }

    return render(request, "books.html" , context)

from django.contrib import messages


def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully.')
            return redirect('books-view')
    else:
        form = BookForm()

    context = {
        'title': 'Create Book',
        'entity': 'Books',
        'page_name': 'Create a new Book',
        'url_list': reverse('books-view'),
        'form': form,
    }

    return render(request, "create.html" , context)

def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('books-view')
    else:
        form = BookForm(instance=book)

    context = {
        'title': 'Update Book',
        'entity': 'Books',
        'page_name': 'Update Book',
        'url_list': reverse('books-view'),
        'form': form,
    }

    return render(request, "create.html" , context)

def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.error(request, 'Book deleted successfully.')
        return redirect('books-view')

    context = {
        'title': 'Delete Book',
        'entity': 'Books',
        'page_name': 'Delete Book',
        'url_list': reverse('books-view'),
        'book': book,
    }

    return render(request, "delete.html" , context)


def book_bulk_create_view(request):
    fake = Faker()
    books = []
    for _ in range(100):
        books.append(Book(
            title=fake.catch_phrase(),
            author=fake.name(),
            publisher=fake.company(),
            published_date=fake.date_this_decade(),
        ))
    Book.objects.bulk_create(books)
    messages.success(request, '100 books created successfully.')
    return redirect('books-view')