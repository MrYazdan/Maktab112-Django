from django.urls import path
from .views import login_view as login, logout_view as logout, register

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', register, name="register"),
    # path('change-password/', change_password),
    # path('forget-password/', forget_password),
    # path('profile/', profile),
]

