from django.db import models
from .behaviours import Timestamps, Slugable
from .utils import category_images, subcategory_images

# Create your models here.


class ProductCategory(Timestamps, Slugable, models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=category_images)



class ProductSubcategory(Timestamps, Slugable, models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name="subcategories")
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=subcategory_images)

