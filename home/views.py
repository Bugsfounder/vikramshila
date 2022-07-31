from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "home/index.html")
