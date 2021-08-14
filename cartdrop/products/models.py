from django.db import models
from cartdrop.core.behaviours import Timestamps, UUIDField
from django.conf import settings
from .utils import product_images
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from string import ascii_uppercase
# Create your models here.



class Product(Timestamps, UUIDField, models.Model):
    brand = models.ForeignKey(
        'core.Brand', on_delete=models.CASCADE, related_name="product_list"
    )
    PID = models.CharField(max_length=50, db_index=True, blank=True)
    product_code = models.CharField(max_length=3, unique=True, default="NCD")
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        'core.ProductSubcategory', on_delete=models.CASCADE, related_name="items"
    )
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=100, blank=True)
    available_stock = models.PositiveIntegerField(default=0)
    overall_rating = models.DecimalField(max_digits=1, decimal_places=1)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            self.PID = self.product_code + get_random_string(length=15, allowed_chars=ascii_uppercase)
        return super().save(*args, **kwargs)
    


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=product_images)