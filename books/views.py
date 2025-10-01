from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Book
from .forms import BookForm


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

def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
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
        return redirect('books-view')

    context = {
        'title': 'Delete Book',
        'entity': 'Books',
        'page_name': 'Delete Book',
        'url_list': reverse('books-view'),
        'book': book,
    }

    return render(request, "delete.html" , context)