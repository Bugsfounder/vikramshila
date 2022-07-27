from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name="Authentication"),
    path("signup", views.signup, name="Signup"),
    path("login", views.login, name="Login"),
    path("logout", views.logout, name="Logout")
]
