from django.contrib import admin
from django.db.models.base import Model
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('category_name',),
    }
    list_display = ['category_name', 'slug']

admin.site.register(Categories, CategoryAdmin)