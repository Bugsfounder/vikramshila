from django.contrib import admin
from .models import Categorie, CategorieItem, Item

# Register your models here.
admin.site.register(Categorie)
admin.site.register(CategorieItem)
admin.site.register(Item)
