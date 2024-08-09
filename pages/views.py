from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# def hi(request, endpoint, name):  # For re_path
    # print("Endpoint:", endpoint)
def hi(request, name):
    return render(request, "hi.html", context={
        "name": name,
        "numbers": range(100)
    })
