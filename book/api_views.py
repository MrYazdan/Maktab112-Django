from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from .models import Book

from .serializers import BookSerializer


# 1) APIView
# class BooksAPIView(APIView):
#     def get(self, request):
#         return Response(Book.objects.values(), status=200)
#
#     def post(self, request):
#         data = request.data
#         return Response({"data": data}, status=201)

# 2) GenericAPIView
# class BooksGenericView(generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         pass

# 3) GenericAPIView + Mixin
# class BookListAPIView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)

# 4) Generic Views
# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# 5) Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
