from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

# Create your models here.
# ex: services, jobs, product  etc
class Categorie(models.Model):
    title = models.CharField(max_length=120, unique=True, primary_key=True)
    description = models.TextField()
    slug = models.SlugField(default="/")
    image = models.ImageField(upload_to="category/", null=True, blank=True)
    datetime = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title

# ex: CorelDraw, Excel, Photoshop, work etc 
class CategorieItem(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="categoryItem/", null=True, blank=True, default="defaultItem.jpg")
    slug = models.SlugField(default="listCategory")
    description = models.TextField()
    datetime = datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# ex: typing 10 page, pen , book , copy, etc
class ItemModel(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    categoryItem = models.ForeignKey(CategorieItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    image = models.ImageField(upload_to="Item/", null=True, blank=True, default="defaultItem.jpg")
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(default="item")
    contact = models.CharField(default="+919905450440", max_length=20)
    price= models.IntegerField()
    datetime = datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."