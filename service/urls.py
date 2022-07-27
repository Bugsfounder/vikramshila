from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name="Service"),
    path("typing", views.typing, name="Typing")
]
