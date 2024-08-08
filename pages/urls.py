from .views import home, about
from django.urls import path

urlpatterns = [
    path('', home),
    path('about/', about)
]
