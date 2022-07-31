from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate
from django.contrib.auth  import  login as db_login
from django.contrib.auth  import  logout as db_logout

# Create your views here.
def auth(request):
    return render(request, "userAuth/auth.html")

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['confirmPassword']

        # Checking if user is exists or not
        if User.objects.filter(username=username).exists():
            messages.error(request, " Username already exists use another username. ex: username123, username@432","danger")
            return render( request,'userAuth/auth.html')
        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters","danger")
            return render( request,'userAuth/auth.html')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers","danger")
            return render( request,'userAuth/auth.html')
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return render( request,'userAuth/auth.html')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.username= username
        myuser.save()
        messages.success(request, " Your vikramshila id has been successfully created")
        return render(request, "userAuth/login.html")
    messages.error(request, "Something went wrong","danger")
    return render( request,'userAuth/auth.html')

def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginemail=request.POST['email']
        loginpassword=request.POST['password']

        user=authenticate(username=loginusername, email=loginemail, password=loginpassword)
        if user is not None:
            db_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again","danger")
            return render(request, 'userAuth/login.html')

    messages.error(request, "Something went wrong","danger")
    return render(request, 'userAuth/login.html')


def logout(request):
    db_logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')
