import json

from book.models import Author
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed

from book.serializers import AuthorSerializer


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


@api_view(['GET', 'POST'])
def author_list_creation(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
