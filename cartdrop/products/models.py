from string import ascii_uppercase

from django.conf import settings
from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from cartdrop.core.behaviours import Slugable, Timestamps, UUIDField

from .utils import product_images

# Create your models here.

class ProductColor(Slugable ,models.Model):
    name = models.CharField(max_length=100)

# Display type for mobile like HD, HD+, Super AMOLED etc
class DisplayType(models.Model):
    name = models.CharField(max_length=200)

# Mobile Variant like 6gb/64gb, 8gb/128gb etc
class MobileVariants(models.Model):
    name = models.CharField(max_length=200, db_index=True)


# Operating System like Android, Windows Mac OS for mobiles and laptops and other products that has operating system
class OperatingSystem(Slugable ,models.Model):
    name = models.CharField(max_length=100, db_index=True)

# Screen Type eg LCD LED
class ScreenType(models.Model):
    name = models.CharField(max_length=100)

class ProductMobileFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    display_type = models.ForeignKey(DisplayType, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=100)
    sim_type = models.CharField(max_length=100)
    touchscreen = models.BooleanField(default=True)
    smart_phone = models.BooleanField(default=True)
    battery_capicity = models.CharField(max_length=6)
    os = models.ForeignKey(OperatingSystem, on_delete=SET_NULL, null=True, blank=True)
    variant = models.ForeignKey(MobileVariants, on_delete=models.SET_NULL, null=True, blank=True)


class ProductLaptopFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    display_type = models.ForeignKey(DisplayType, on_delete=models.CASCADE)
    os = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=100)
    battery_backup = models.CharField(max_length=100)
    touchscreen = models.BooleanField(default=True)
    storage = models.CharField(max_length=100)


class ProductTelivisionFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    screen_type = models.ForeignKey(ScreenType, on_delete=models.CASCADE)
    is_3d = models.BooleanField(default=False)
    is_curved = models.BooleanField(default=False)
    has_wify = models.BooleanField(default=True)
    usb_count = models.PositiveIntegerField(default=0)

    

class ProductSpecification(models.Model):
    in_box = models.CharField(max_length=1000)
    launched_date = models.DateField(auto_now=True)
    model_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True)
    mobile = models.OneToOneField(ProductMobileFeatures, on_delete=models.SET_NULL, null=True, blank=True)
    laptop = models.OneToOneField(ProductLaptopFeatures, on_delete=models.SET_NULL, null=True, blank=True)
    tv = models.OneToOneField(ProductTelivisionFeatures, on_delete=models.SET_NULL, null=True, blank=True)


class Product(Timestamps, UUIDField, models.Model):
    brand = models.ForeignKey(
        "core.Brand", on_delete=models.CASCADE, related_name="product_list"
    )
    PID = models.CharField(max_length=50, db_index=True, blank=True, help_text="A Unique Product Identification Number")
    product_code = models.CharField(max_length=3, unique=True, default="NCD")
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        "core.ProductSubcategory", on_delete=models.CASCADE, related_name="items"
    )
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    available_stock = models.PositiveIntegerField(default=0)
    overall_rating = models.DecimalField(max_digits=1, decimal_places=1)
    color = models.ForeignKey(ProductColor, on_delete=SET_NULL, null=True)
    specification = models.OneToOneField(ProductSpecification, null=True, blank=True, on_delete=models.SET_NULL)
    replacement_days = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
            self.PID = self.product_code + get_random_string(
                length=15, allowed_chars=ascii_uppercase
            )
        return super().save(*args, **kwargs)


class ProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=product_images)
