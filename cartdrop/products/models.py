from string import ascii_uppercase

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from cartdrop.core.behaviours import Slugable, Timestamps, UUIDField

from .utils import product_images, product_images_placeholder

# Create your models here.


class ProductColor(Slugable):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ScreenType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Display type for mobile like HD, HD+, Super AMOLED etc
class DisplayType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Mobile Variant like 6gb/64gb, 8gb/128gb etc
class MobileVariant(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


class LaptopVariant(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


class TVVariant(models.Model):
    display_size = models.CharField(max_length=100)

    def __str__(self):
        return self.display_size + " Inches"


class ACCapacityVariant(models.Model):
    capacity = models.CharField(max_length=100)

    def __str__(self):
        return self.capacity


class ACStarRatingVariant(models.Model):
    star = models.CharField(max_length=100)

    def __str__(self):
        return self.star


class BookVariant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Operating System like Android, Windows Mac OS for mobiles and laptops and other products that has operating system
class OperatingSystem(Slugable):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


# Washing Methods Types
class WashingMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# AC type eg split, window etc
class ACType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductSeries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Refrigerator type example Single Door , Double Door etc
class RefrigeratorType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Speaker type example Speaker, Home Theatre, Blootooth Speaker
class SpeakerType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SimType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProductMobileFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    display_type = models.ForeignKey(DisplayType, on_delete=models.CASCADE)
    resolution = models.CharField(max_length=100)
    sim_type = models.ForeignKey(
        SimType, on_delete=models.SET_NULL, null=True, blank=True
    )
    touchscreen = models.BooleanField(default=True)
    smart_phone = models.BooleanField(default=True)
    battery_capicity = models.CharField(max_length=20)
    os = models.ForeignKey(OperatingSystem, on_delete=SET_NULL, null=True, blank=True)
    ram = models.CharField(max_length=100)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE, null=True)

    def __str__(self):
        s = ", ".join(
            [
                self.series.name,
                self.display_size,
                self.resolution,
                self.os.name,
                self.ram,
                self.sim_type.name,
            ]
        )
        return s


class ProductLaptopFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    display_type = models.ForeignKey(DisplayType, on_delete=models.CASCADE)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE)
    os = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    processor = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    battery_backup = models.CharField(max_length=100)
    touchscreen = models.BooleanField(default=True)

    def __str__(self):
        return self.series.name


class ProductTelivisionFeatures(models.Model):
    display_size = models.CharField(max_length=100)
    series = models.ForeignKey(
        ProductSeries, on_delete=models.SET_NULL, null=True, blank=True
    )
    screen_type = models.ForeignKey(ScreenType, on_delete=models.CASCADE)
    is_3d = models.BooleanField(default=False)
    is_curved = models.BooleanField(default=False)
    has_wify = models.BooleanField(default=True)
    usb_count = models.PositiveIntegerField(default=0)
    refresh_rate = models.CharField(max_length=100, null=True)
    includes_wallmount = models.BooleanField(default=False)

    def __str__(self):
        return self.series.name


class ProductWashingMachineFeatures(models.Model):
    energy_rating = models.PositiveIntegerField(
        default=3, validators=[MaxValueValidator(5)]
    )
    washing_capicity = models.PositiveIntegerField(default=0)
    washing_method = models.ForeignKey(
        WashingMethod, on_delete=models.SET_NULL, null=True, blank=True
    )
    has_inbuilt_heater = models.BooleanField(default=False)


class ProductAirConditionerFeature(models.Model):
    type = models.ForeignKey(ACType, on_delete=models.SET_NULL, null=True, blank=True)
    compressor = models.CharField(max_length=100)
    cooling_capacity = models.PositiveIntegerField(default=0)
    series = models.ForeignKey(
        ProductSeries, on_delete=models.SET_NULL, null=True, blank=True
    )
    cooling_coverage_area = models.CharField(max_length=100, blank=True)


class ProductRefrigeratorFeature(models.Model):

    capacity = models.CharField(max_length=100)
    energy_rating = models.PositiveIntegerField(
        default=3, validators=[MaxValueValidator(5)]
    )
    compressor_type = models.CharField(max_length=100)
    type = models.ForeignKey(RefrigeratorType, on_delete=models.CASCADE)
    stabilizer_required = models.BooleanField(default=False)


class ProductSpeakersFeatures(models.Model):
    power_output = models.CharField(max_length=20, blank=True)
    frequency_response = models.CharField(max_length=100, blank=True, null=True)
    has_bluetooth = models.BooleanField(default=False)
    type = models.ForeignKey(SpeakerType, on_delete=models.CASCADE)


class ProductSpecification(models.Model):
    in_box = models.CharField(max_length=1000)
    launched_date = models.DateField(auto_now=True)
    model_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.OneToOneField(
        ProductMobileFeatures, on_delete=models.SET_NULL, null=True, blank=True
    )
    laptop = models.OneToOneField(
        ProductLaptopFeatures, on_delete=models.SET_NULL, null=True, blank=True
    )
    tv = models.OneToOneField(
        ProductTelivisionFeatures, on_delete=models.SET_NULL, null=True, blank=True
    )
    washing_machine = models.OneToOneField(
        ProductWashingMachineFeatures, on_delete=models.SET_NULL, null=True, blank=True
    )
    ac = models.OneToOneField(
        ProductAirConditionerFeature, on_delete=models.SET_NULL, null=True, blank=True
    )
    refrigerator = models.OneToOneField(
        ProductRefrigeratorFeature, on_delete=models.SET_NULL, null=True, blank=True
    )
    speaker = models.OneToOneField(
        ProductSpeakersFeatures, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.model_name


class ProductWarranty(models.Model):
    summary = models.CharField(max_length=200)
    covered = models.TextField(max_length=500, blank=True)
    not_covered = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.summary


class Product(Timestamps, UUIDField):
    brand = models.ForeignKey(
        "core.Brand", on_delete=models.CASCADE, related_name="product_list"
    )
    product_code = models.CharField(max_length=3, default="NCD")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True, blank=True)
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    subcategory = models.ForeignKey(
        "core.ProductSubcategory", on_delete=models.CASCADE, related_name="items"
    )
    description = models.TextField(max_length=100, blank=True, null=True)
    overall_rating = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, default=0.0
    )
    replacement_days = models.PositiveIntegerField(default=0)
    warranty = models.ForeignKey(
        ProductWarranty, on_delete=models.SET_NULL, null=True, blank=True
    )
    weight = models.CharField(max_length=100, default=0)
    specification = models.OneToOneField(
        ProductSpecification,
        on_delete=models.SET_NULL,
        null=True,
        related_name="get_product",
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Size ofr clothing like SM, XL, XXL,
class FashionSize(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.code


class ProductVariation(UUIDField):
    pid = models.CharField(
        max_length=50,
        db_index=True,
        blank=True,
        help_text="A Unique Product Identification Number",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variations"
    )
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color = models.ForeignKey(
        ProductColor, on_delete=models.SET_NULL, null=True, blank=True
    )
    active = models.BooleanField(default=True, db_index=True)
    available_stock = models.PositiveIntegerField(default=0)
    mobile_variant = models.ForeignKey(
        MobileVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    laptop_variant = models.ForeignKey(
        LaptopVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    tv_variant = models.ForeignKey(
        TVVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    ac_capacity_variant = models.ForeignKey(
        ACCapacityVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    refrigerator_capacity = models.CharField(max_length=100, null=True, blank=True)
    ac_star_variant = models.ForeignKey(
        ACStarRatingVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    book_variation = models.ForeignKey(
        BookVariant, on_delete=models.SET_NULL, null=True, blank=True
    )
    juices_quantity = models.CharField(max_length=100, null=True, blank=True)
    size = models.ForeignKey(
        FashionSize, on_delete=models.SET_NULL, null=True, blank=True
    )
    images = models.ManyToManyField(
        "products.ProductImages", related_name="for_variations", blank=True
    )

    class Meta:
        ordering = ("-product__created",)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pid = self.product.product_code + get_random_string(
                length=15, allowed_chars=ascii_uppercase
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        variant = (
            self.mobile_variant.name
            if hasattr(self.mobile_variant, "name")
            else self.laptop_variant.name
            if hasattr(self.laptop_variant, "name")
            else self.tv_variant.display_size + " inch"
            if hasattr(self.tv_variant, "display_size")
            else None
        )
        size = self.size.code if hasattr(self.size, "code") else None
        color = self.color.name if hasattr(self.color, "name") else None
        ac_star_variant = (
            self.ac_star_variant.star if hasattr(self.ac_star_variant, "star") else None
        )
        ac_capacity_variant = (
            self.ac_capacity_variant.capacity
            if hasattr(self.ac_capacity_variant, "capacity")
            else None
        )
        refrigerator_capacity = self.refrigerator_capacity
        juices_quantity = self.juices_quantity
        book_variation = (
            self.book_variation.name if hasattr(self.book_variation, "name") else None
        )
        if (
            not variant
            and not size
            and not color
            and not ac_star_variant
            and not ac_capacity_variant
            and not refrigerator_capacity
            and not juices_quantity
            and not book_variation
        ):
            return self.product.name
        s = f"({', '.join([i for i in [color, variant, size, ac_star_variant, ac_capacity_variant, refrigerator_capacity, juices_quantity, book_variation] if i])})"
        return f"{self.product.name} {s if s else ''}"


class ProductImages(models.Model):
    image_summary = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=product_images)
    placeholder = models.ImageField(
        upload_to=product_images_placeholder, default="default_placeholder.jpg"
    )
    primary = models.BooleanField(default=False)

    def __str__(self):
        return self.image_summary


class ProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
