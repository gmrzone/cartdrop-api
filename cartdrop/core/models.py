from django.db import models

from .behaviours import Slugable, Timestamps, UUIDField
from .utils import category_images, subcategory_images

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
