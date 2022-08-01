from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import Contact, Categorie, CategorieItem, ItemModel ,Orders, OrderUpdate
from math import ceil
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
from django.http import HttpResponse
import json

MERCHANT_KEY = 'Your-Merchant-Key-Here'

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

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def productView(request, myid):

    # Fetch the product using the id
    product = ItemModel.objects.filter(id=myid)
    allItems = ItemModel.objects.all()
    isProduct = product[0].category.title == "Products"
    print(isProduct)
    return render(request, 'shop/prodView.html', {'product':product[0],"allItems":allItems,"isProduct":isProduct})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'Your-Merchant-Id-Here',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
    price = request.GET.get('price')
    return render(request, 'shop/checkout.html',{"price":price})


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})