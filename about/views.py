from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def about(request):
    return render(request, "about/aboutwebsite.html")


def author(request):
    return render(request, "about/aboutauthor.html")
