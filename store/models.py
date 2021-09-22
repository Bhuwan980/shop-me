from django.db import models
from categories.models import Categories
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'images/products')
    stock = models.IntegerField()
    is_available = models.BooleanField( default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_product_slug(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __st__(self):
        return self.product_name