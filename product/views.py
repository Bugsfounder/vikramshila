from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def product(request):
    return HttpResponse("this is product page")


def item(request):
    return HttpResponse("This is item page of product")
