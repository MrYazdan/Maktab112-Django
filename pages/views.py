from django.views import View
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


class Home(View):
    def get(self, request):
        return render(self.request, "home.html")
