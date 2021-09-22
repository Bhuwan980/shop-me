from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'stock','price', 'is_available' ]
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)