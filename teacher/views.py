from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "t_home.html")


def index(request):
    return render(request, "home.html")


def login(request):
    return render(request, "t_login.html")


def help(request):
    return render(request, "help.html")


def about(request):
    return render(request, "about.html")
