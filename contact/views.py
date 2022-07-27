from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def contact(request):
    return HttpResponse("this is contact page")


def author(request):
    return HttpResponse("this is contact to author page")
