from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .behaviours import Slugable, Timestamps, UUIDField
from .utils import (brand_photo_location, brand_photo_placeholder_location,
                    category_images, category_images_placeholder,
                    review_image_location, review_image_placeholder_location,
                    subcategory_images, subcategory_images_placeholder)

# Create your models here.


class ProductCategory(Timestamps, Slugable, UUIDField):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="category_images"
    )
    image = models.ImageField(upload_to=category_images)
    placeholder = models.ImageField(
        upload_to=category_images_placeholder, default="default_placeholder.jpg"
    )


class ProductSubcategory(Timestamps, Slugable, UUIDField):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="subcategories",
    )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SubcategoryImage(models.Model):
    subcategory = models.ForeignKey(
        ProductSubcategory, on_delete=models.CASCADE, related_name="subcategory_images"
    )
    image = models.ImageField(upload_to=subcategory_images)
    placeholder = models.ImageField(
        upload_to=subcategory_images_placeholder, default="default_placeholder.jpg"
    )


class Brand(UUIDField, Slugable):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=brand_photo_location)
    placeholder = models.ImageField(
        upload_to=brand_photo_placeholder_location, default="default_placeholder.jpg"
    )

    def __str__(self):
        return self.name


class ProductReview(UUIDField, Timestamps):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="reviews"
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
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)


class ReviewImages(models.Model):
    review = models.ForeignKey(
        ProductReview, on_delete=models.CASCADE, related_name="review_images"
    )
    image = models.ImageField(upload_to=review_image_location)
    placeholder = models.ImageField(
        upload_to=review_image_placeholder_location, default="default_placeholder.jpg"
    )


# Intermediary model between Coupon and user to track when the user applier co
class UserCouponIntermidiary(Timestamps):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_rel")
    coupon = models.ForeignKey("CouponCode", on_delete=models.CASCADE, related_name="coupon_rel")

    
class CouponCode(UUIDField, Timestamps):
    class CouponReusableTypeChoises(models.TextChoices):
        SINGLE = "SINGLE", "Single"
        MONTHLY = "MONTHLY", "Monthly"
        YEARLY = "YEARLY", "Yearly"

    code = models.CharField(max_length=20, db_index=True)
    reusable_type = models.CharField(
        max_length=200,
        default=CouponReusableTypeChoises.SINGLE,
        choices=CouponReusableTypeChoises.choices,
    )
    summary = models.CharField(max_length=200, null=True)
    subcategory = models.ManyToManyField(ProductSubcategory, related_name="coupons")
    discount = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through=UserCouponIntermidiary, symmetrical=False, related_name="coupon_codes")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
