from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.base import Model

from .behaviours import Slugable, Timestamps, UUIDField
from .utils import (brand_photo_location, category_images, product_images,
                    review_image_location, subcategory_images)

# Create your models here.


class ProductCategory(Timestamps, Slugable, UUIDField, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="category_images"
    )
    image = models.ImageField(upload_to=category_images)


class ProductSubcategory(Timestamps, Slugable, UUIDField, models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=subcategory_images)


class Brand(UUIDField, Slugable, models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=brand_photo_location)


class Product(Timestamps, Slugable, UUIDField, models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="product_list"
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="items"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=100, blank=True)


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=product_images)


class ProductReview(UUIDField, Timestamps, models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_review",
    )
    review = models.TextField(max_length=500, blank=True)
    stars = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_certified_buyer = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


class ReviewImages(models.Model):
    review = models.ForeignKey(
        ProductReview, on_delete=models.CASCADE, related_name="review_images"
    )
    image = models.ImageField(upload_to=review_image_location)
