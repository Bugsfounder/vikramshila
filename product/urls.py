from django.urls import path
from . import views

urlpatterns = [
    path("", views.product, name="Products"),
    path("item", views.item, name="Item of Product")
]
