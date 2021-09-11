from django.shortcuts import render, redirect

from online_library.book.forms import BookForm, DeleteBookForm
from online_library.book.models import Book
from online_library.user.forms import UserForm
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
    user = User.objects.get()
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    context = {
        'form': form,
        'user': user,
    }

    return render(req, 'add-book.html', context)

def edit_book(req, pk):
    book = Book.objects.get(pk=pk)
    user = User.objects.get()

    if req.method == 'POST':
        form = BookForm(req.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
        'book': book,
        'user': user
    }

    return render(req, 'edit-book.html', context)

def book_details(req, pk):
    user = User.objects.get()
    book = Book.objects.get(pk=pk)

    context = {
        'user': user,
        'book': book,
    }

    return render(req, 'book-details.html', context)

def delete_book(req, pk):
    book = Book.objects.get(pk=pk)
    user = User.objects.get()

    if req.method == 'POST':
        book.delete()

        return redirect('home')

    else:
        form = DeleteBookForm(instance=book)

    context = {
        'book': book,
        'user': user,
        'form': form,
    }

    return render(req, 'delete-book.html', context)