from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="Contact"),
    path("author", views.author, name="Contact To Author")
]
