from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_store_all_data, name="StoreAllData"),
    path('jobscat', views.jobscat, name="Store Jobs Categories"),
    path("servicecat", views.servicecat, name="Store Service Categories"),
    path('productcat', views.productcat, name="Store Product Categories"),
]