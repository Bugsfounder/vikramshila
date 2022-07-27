from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('author', views.author, name="About Author")
]
