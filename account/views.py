from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseBadRequest, HttpResponse


def login_view(request):
    if request.method == "GET":
        return render(request, "account/login.html")

    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('/')

        # if username and password and User.objects.filter(username=username).exists():
        #     user = User.objects.get(username=username)
        #     if user.check_password(password):
        #         login(request, user)
        #         return redirect("/")

        return HttpResponseBadRequest("Invalid username or password.")


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        return render(request, "account/register.html")

    elif request.method == "POST":
        try:
            password = request.POST.get("password", None)
            assert password, "Password is required"

            confirm = request.POST.get("confirm_password", None)
            assert confirm, "Confirm password are required"

            assert len(password) > 6 and password.isalnum(), "Password must be at least 6 characters long."
            assert password == confirm, "Passwords do not match."

            username = request.POST.get("username", None)
            assert username, "Username is required"

            User.objects.create_user(username=username, password=password)

            return HttpResponse("User has been created successfully !", status=201)

        except AssertionError as e:
            return HttpResponseBadRequest(e)

        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Uncaught error ...")
