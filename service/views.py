from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def service(request):
    return HttpResponse("this is service page")


def typing(request):
    return HttpResponse("this is typing service page")
