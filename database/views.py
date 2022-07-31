from django.shortcuts import render, HttpResponse
from jobs.models import Categorie as JobCategorie
from service.models import ServiceCategorie
from product.models import ProductCategorie
from service.models import ServiceCategorie

# Create your views here.
def db_store_all_data(request):
    return HttpResponse("db_store_all_data")

def jobscat(request):
    return HttpResponse("jobscat")

def servicecat(request):
    return HttpResponse("servicecat")
    
def productcat(request):
    return HttpResponse("productcat")