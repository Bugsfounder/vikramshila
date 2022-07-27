from django.urls import path
from . import views

urlpatterns = [
    path("", views.jobs, name="Jobs"),
    path("typist", views.typist, name="Typies Job")
]
