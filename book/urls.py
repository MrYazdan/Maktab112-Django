# from .views import books, book_list_creation
# from .views import books, Books, BookCreateView, BookDetailView
from rest_framework.routers import DefaultRouter
from .api_views import BookViewSet
from django.urls import path

router = DefaultRouter()
router.register('api/books', BookViewSet)

urlpatterns = [
    # path('books/', books, name="books_list_create"),
    # path('books/', Books.as_view(), name="books_list_create"),
    # path('books/', BookCreateView.as_view(), name="books_list_create"),
    # path('books/<pk>', BookDetailView.as_view(), name="book_detail"),
    # path('api/books/', book_list_creation, name="books_list_create"),

    # api:
    # path("api/books", BooksAPIView.as_view())
    # path("api/books", BooksGenericView.as_view())
    # path("api/books", BookListAPIView.as_view())
    # path("api/books", BookListCreateAPIView.as_view()),
    # path("api/books/<pk>", BookRetrieveUpdateDeleteAPIView.as_view())
]

urlpatterns += router.urls
