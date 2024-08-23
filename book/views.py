from book.models import Book
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def books(request):
    if request.method == "POST":
        form_data = request.POST

        try:
            title = form_data.get('name')
            price = form_data.get('price')
            Book.objects.create(title=title, price=price, published_date="2020-01-01")
        except Exception as e:
            print(e)
            return HttpResponse("Bad request !", status=400)

        return HttpResponse("OK", status=201)


    return render(request, "books.html", dict(books=Book.objects.all()))
