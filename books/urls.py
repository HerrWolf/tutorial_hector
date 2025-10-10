from django.urls import path
from .views import books_view, book_create_view, book_update_view, book_delete_view, book_bulk_create_view


urlpatterns = [
    path('', books_view, name='books-view'),
    path('create/', book_create_view, name='book-create-view'),
    path('update/<int:pk>/', book_update_view, name='book-update-view'),
    path('delete/<int:pk>/', book_delete_view, name='book-delete-view'),
    path('bulk_create/', book_bulk_create_view, name='book-bulk-create-view'),
]
