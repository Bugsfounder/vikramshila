from email.policy import default
from django.db import models
from django.utils import timezone

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
class Item(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    categoryItem = models.ForeignKey(CategorieItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Item/", null=True, blank=True, default="defaultItem.jpg")
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(default="item")
    contact = models.CharField(default="+919905450440", max_length=20)
    price= models.IntegerField()
    datetime = datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

