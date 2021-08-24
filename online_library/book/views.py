from django.shortcuts import render, redirect

from online_library.book.models import Book
from online_library.user.models import User


def home(req):
    user = User.objects.first()

    if not user:
        return redirect('create user')

    books = Book.objects.all()
    user = User.objects.get()
    context = {
        'books': books,
        'user': user,
    }

    return render(req, 'home-with-profile.html', context)


def add_book(req):
    pass

def edit_book(req, pk):
    pass

def book_details(req, pk):
    pass

def book_delete(req, pk):
    pass