from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def jobs(request):
    return HttpResponse("this is jobs page")


def typist(request):
    return HttpResponse("this is typist jobs page")
