from django.db import models
from cartdrop.core.behaviours import Timestamps, Slugable, UUIDField
from django.conf import settings
from .utils import product_images
# Create your models here.



class Product(Timestamps, Slugable, UUIDField, models.Model):
    brand = models.ForeignKey(
        'core.Brand', on_delete=models.CASCADE, related_name="product_list"
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        'core.ProductSubcategory', on_delete=models.CASCADE, related_name="items"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=100, blank=True)
    available_stock = models.PositiveIntegerField(default=0)
    overall_rating = models.DecimalField(max_digits=1, decimal_places=1)
    PID = models.CharField(max_length=50, db_index=True, blank=True)
    


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=product_images)