from django.shortcuts import render, redirect

from online_library.user.models import User


def home(req):
    user = User.objects.first()

    if not user:
        return redirect('create user')


def add_book(req):
    pass

def edit_book(req, pk):
    pass

def book_details(req, pk):
    pass

def book_delete(req, pk):
    pass