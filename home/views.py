from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import Contact, Categorie, CategorieItem, ItemModel
from math import ceil
from django.db.models import Q

# Create your views here.
def index(request):
    allCategories = Categorie.objects.all()
    return render(request, "home/index.html",{"categories":allCategories})

def about(request):
    return render(request, "home/aboutauthor.html")

def website(request):
    return render(request, "home/aboutwebsite.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        description =request.POST['description']
        if Contact.objects.filter(name=name).exists():
            messages.error(request, " Username already exists in database use another username. ex: username123, username@432","danger")
            return render(request, "contact/contact.html")
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(description)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, description=description)
            contact.save()
            messages.success(request, "Your message has been successfully sent. we reply you as soon as possible")
    return render(request, "home/contact.html")


def listCategory(request):
    category = request.POST['category']
    desc = request.POST['description']
    allItems = CategorieItem.objects.filter(category=category)
    return render(request, "home/listCategorie.html", {"allItems":allItems, "category_":category,"desc":desc})

def item(request):
    if request.method=="POST":
        category = request.POST['category']
        categoryItem = request.POST['categoryItem']
        desc = request.POST['description']
        isProduct = category=="Products"
        allItems = ItemModel.objects.all()
        allItemsRelatedToCat = []
        for item in allItems:
            if (item.category.title == category )and( item.categoryItem.title==categoryItem):
                allItemsRelatedToCat.append(item)
        return render(request, "home/item.html", {"allItems":allItems,"allItemsRelatedToCat":allItemsRelatedToCat, "title":categoryItem, "category":category,"desc":desc,"isProduct":isProduct})

def search(request):
    query=request.POST['query']
    results = ItemModel.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
    params = {'msg':"All Search Results" , "len":len(results)}
    if len(results)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'home/search.html', {"results":results,"params":params})


def delete(request):
    return HttpResponse("DELETING....")