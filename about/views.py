from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def about(request):
    return HttpResponse("this is about page")


def author(request):
    return HttpResponse("this is about author page")
