from .views import home, Home
from django.urls import path, re_path

urlpatterns = [
    # path('', home),
    path('', Home.as_view()),
    # path('about/', about),
    # re_path(r'^(hello|hi|slm|salam)/(?P<name>\w)/$', hi),
    # path('hello/<str:name>/', hi)
]

