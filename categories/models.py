from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=100, unique=True)
    cat_description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='images/categories')

    class Meta:
        verbose_name_plural = "categories"

    def get_slug(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name