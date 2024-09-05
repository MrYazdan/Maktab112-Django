from .views import books
from django.urls import path

urlpatterns = [
    path('books/', books),
]

