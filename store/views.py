from django.shortcuts import render, get_object_or_404
from .models import *
from categories.models import *

# Create your views here.
def store(request, slug=None):
    products = None
    category=None

    if slug !=None:
        category = get_object_or_404(Categories, slug=slug)
        products = Product.objects.all().filter(category=category,is_available=True)
        products_count = products.count()

    else:
             
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    context = {
        'products': products,
        'products_count': products_count
        
    }
    return render(request, 'store/store.html', context)


#first slug is for category 
def product_detail(request, slug, product_slug):

    product = Product.objects.get(slug=product_slug)
    
    context = {
        'product': product
    }
    return render(request, 'store/product-detail.html', context)