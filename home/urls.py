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
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
