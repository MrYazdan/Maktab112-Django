from django.shortcuts import render

from products.models import Product


def products(request):
    return render(request, "products.html", dict(
        products=Product.objects.filter(price__gt=10000)
    ))
