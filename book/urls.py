from .views import books, book_list_creation
from django.urls import path


urlpatterns = [
    path('books/', books),
    path('api/books/', book_list_creation, name="books_list_create"),
]

