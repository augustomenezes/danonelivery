from django.contrib import admin
from .models import Product
from .models import User

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)


admin.site.register(User)
