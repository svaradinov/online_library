from django.urls import path

from online_library.user.views import create_user, delete_user, edit_user, user_details

urlpatterns = [
    path('', user_details, name='user details'),
    path('edit/', edit_user, name='edit user'),
    path('delete/', delete_user, name='delete user'),
    path('create/', create_user, name='create user'),
]