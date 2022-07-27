"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls"), name="home"),
    path('about/', include("about.urls"), name="about"),
    path('contact/', include('contact.urls'), name="contact"),
    path('service/', include('service.urls'), name="service"),
    path('product/', include('product.urls'), name="product"),
    path('auth/', include('userAuth.urls'), name="auth"),
    path('jobs/', include('jobs.urls'), name="jobs")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler500 = 'errors.views.error_500' # implement later
