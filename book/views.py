import json
from django.views import View
from book.models import Author, Book
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from book.serializers import AuthorSerializer, BookSerializer
from django.views.generic import ListView, CreateView, list, DetailView


# def books(request):
#     if request.method == "POST":
#         form_data = request.POST
#
#         try:
#             title = form_data.get('name')
#             price = form_data.get('price')
#             Book.objects.create(title=title, price=price, published_date="2020-01-01")
#         except Exception as e:
#             print(e)
#             return HttpResponse("Bad request !", status=400)
#
#         return HttpResponse("OK", status=201)
#
#     return render(request, "books.html", dict(books=Book.objects.all()))


# class Books(View):
#     def post(self, request):
#         form_data = self.request.POST
#
#         try:
#             title = form_data.get('name')
#             price = form_data.get('price')
#             Book.objects.create(title=title, price=price, published_date="2020-01-01")
#         except Exception as e:
#             print(e)
#             return HttpResponse("Bad request !", status=400)
#
#         return HttpResponse("OK", status=201)
#
#     def get(self, request):
#         return render(self.request, "books.html", dict(books=Book.objects.all()))


# before using DRF
# @csrf_exempt
# def author_list_creation(request):
#     if request.method == "GET":
#         # get all authors:
#         authors = list(Author.objects.values())
#         return JsonResponse(authors, safe=False)
#
#     elif request.method == "POST":
#         data = json.loads(request.body)
#         author = Author.objects.create(name=data['name'])
#         return JsonResponse({'id': author.id, 'name': author.name}, status=201)
#
#     else:
#         return HttpResponseNotAllowed(['GET', 'POST'])

# @api_view(['GET', 'POST'])
# def author_list_creation(request):
#     if request.method == "GET":
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=400)


# def books(request):
#     return render(request, "books.html", dict(books=Book.objects.all()))


# @api_view(['GET', 'POST'])
# def book_list_creation(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=400)


def books(request):
    return render(request, "books.html", dict(books=Book.objects.all()))


class Books(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"


# class BookCreateView(CreateView, list.BaseListView):
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'cover_image', 'price']
    template_name = "books.html"
    extra_context = {
        "books": Book.objects.all()
    }
    success_url = '/books'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = self.model.objects.all()
    #
    #     return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


