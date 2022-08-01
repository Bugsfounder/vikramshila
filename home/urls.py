from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('listCategory/', views.listCategory, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('item/', views.item, name="contact"),
    path('search/', views.search, name="search"),
    path('delete/', views.delete, name="delete"),
]
