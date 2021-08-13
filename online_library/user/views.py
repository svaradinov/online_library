from django.shortcuts import render

from online_library.user.models import User


def create_user(req):
    user = User.objects.get()


def user_details(req):
    pass

def edit_user(req):
    pass

def delete_user(req):
    pass