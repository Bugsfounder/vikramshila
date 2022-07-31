from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        description =request.POST['description']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(description)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, description=description)
            contact.save()
            messages.success(request, "Your message has been successfully sent. we reply you as soon as possible")
    return render(request, "contact/contact.html")



