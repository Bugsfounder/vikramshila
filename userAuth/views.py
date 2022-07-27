from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def auth(request):
    return HttpResponse("This is Authentication Page")


def signup(request):
    return HttpResponse("This is signup Page")


def login(request):
    return HttpResponse("This is login Page")


def logout(request):
    return HttpResponse("This is logout Page")
