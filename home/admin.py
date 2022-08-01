from django.contrib import admin
from .models import Categorie, CategorieItem, ItemModel, Orders, OrderUpdate

# Register your models here.
admin.site.register(Categorie)
admin.site.register(CategorieItem)
admin.site.register(ItemModel)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
