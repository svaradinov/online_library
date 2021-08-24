from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_library.book.urls')),
    path('user', include('online_library.user.urls')),
]
