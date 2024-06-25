from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def flights(request):
    return render(request, "flights.html")


def contacts(request):
    return render(request, "contacts.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в систему")
            return redirect("home")
        else:
            messages.error(request, "Неверные учетные данные")
    return redirect("home")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Имя пользователя уже занято")
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Электронная почта уже зарегистрирована")
            else:
                user = CustomUser.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                login(request, user)
                messages.success(request, "Регистрация прошла успешно")
                return redirect("home")
        else:
            messages.error(request, "Пароли не совпадают")
    return redirect("home")


def user_logout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect("home")
