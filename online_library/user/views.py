from django.shortcuts import render, redirect

from online_library.book.models import Book
from online_library.user.forms import UserForm, DeleteUserForm
from online_library.user.models import User


def create_user(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = UserForm()

    context = {
        'form': form
        }

    return render(req, 'home-no-profile.html', context)


def user_details(req):
    user = User.objects.first()

    context = {
        'user': user
    }

    return render(req, 'profile.html', context)


def edit_user(req):
    user = User.objects.get()

    if req.method == 'POST':
        form = UserForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user details')
    else:
        form = UserForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(req, 'edit-profile.html', context)


def delete_user(req):
    user = User.objects.get()
    books = Book.objects.all()

    if req.method == 'POST':
        user.delete()
        books.delete()

        return redirect('home')
    else:
        form = DeleteUserForm(instance=user)

    context = {
        'form': form,
        'user': user
    }

    return render(req, 'delete-profile.html', context)