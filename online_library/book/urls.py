from django.urls import path

from online_library.book.views import home, add_book, edit_book, book_details, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', book_details, name='book details'),
    path('delete/<int:pk>', delete_book, name='delete book')
]