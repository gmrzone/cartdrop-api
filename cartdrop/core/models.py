from django.db import models

from .behaviours import Slugable, Timestamps, UUIDField
from .utils import category_images, subcategory_images, product_images

# Create your models here.


class ProductCategory(Timestamps, Slugable, UUIDField, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="category_images")
    image =  models.ImageField(upload_to=category_images)

    
class ProductSubcategory(Timestamps, Slugable, UUIDField, models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=subcategory_images)


class Product(Timestamps, Slugable, UUIDField, models.Model):
    name= models.CharField(max_length=100)
    subcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=product_images)