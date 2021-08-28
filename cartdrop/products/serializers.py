from accounts.serializers import SellerUserSerializer
from core.serializers import BrandSerializer, ProductSubcategorySerializer
from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from .models import (DisplayType, OperatingSystem, Product,
                     ProductLaptopFeatures, ProductMobileFeatures,
                     ProductSeries, ProductSpecification,
                     ProductTelivisionFeatures, ProductVariation,
                     ProductWarranty, ProductWashingMachineFeatures,
                     ScreenType, SimType, WashingMethod)


class WashingMethodSerializer(ModelSerializer):
    class Meta:
        model = WashingMethod
        fields = ("name",)


class ScreenTypeSerializer(ModelSerializer):
    class Meta:
        model = ScreenType
        fields = ("name",)


class SimTypeSerializer(ModelSerializer):
    class Meta:
        model = SimType
        fields = ("name",)


class OperatingSystemSerializer(ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = ("name",)


class ProductSeriesSerializer(ModelSerializer):
    class Meta:
        model = ProductSeries
        fields = ("name",)


class DisplayTypeSerializer(ModelSerializer):
    class Meta:
        model = DisplayType
        fields = ("name",)


class MobileFeatureSerializer(ModelSerializer):
    display_type = DisplayTypeSerializer(many=False)
    sim_type = SimTypeSerializer(many=False)
    os = OperatingSystemSerializer(many=False)
    series = ProductSeriesSerializer(many=False)

    class Meta:
        model = ProductMobileFeatures
        fields = (
            "display_size",
            "display_type",
            "resolution",
            "sim_type",
            "touchscreen",
            "smart_phone",
            "battery_capicity",
            "os",
            "ram",
            "series",
        )


class LaptopFeatureSerializer(ModelSerializer):
    display_type = DisplayTypeSerializer(many=False)
    series = ProductSeriesSerializer(many=False)
    os = OperatingSystemSerializer(many=False)

    class Meta:
        model = ProductLaptopFeatures
        fields = (
            "display_size",
            "display_type",
            "series",
            "os",
            "processor",
            "resolution",
            "battery_backup",
            "touchscreen",
        )


class TelevisionFeatureSerializer(ModelSerializer):
    series = ProductSeriesSerializer(many=False)
    screen_type = ScreenTypeSerializer(many=False)

    class Meta:
        model = ProductTelivisionFeatures
        fields = (
            "display_size",
            "series",
            "screen_type",
            "is_3d",
            "is_curved",
            "has_wifi",
            "usb_count",
            "refresh_rate",
            "includes_wallmount",
        )


class WashingMachineFeatureSerializer(ModelSerializer):
    washing_method = WashingMethodSerializer(many=False)

    class Meta:
        model = ProductWashingMachineFeatures
        fields = (
            "energy_rating",
            "washing_capicity",
            "washing_method",
            "has_inbuilt_heater",
        )


class ProductWarrantySerializer(ModelSerializer):
    class Meta:
        models = ProductWarranty
        fields = ("summary", "covered", "not_covered")


class ProductSpecificationSerializer(ModelSerializer):
    laptop = LaptopFeatureSerializer(many=False)
    mobile = MobileFeatureSerializer(many=False)
    tv = TelevisionFeatureSerializer(many=False)
    washing_machine = WashingMachineFeatureSerializer(many=False)

    class Meta:
        model = ProductSpecification
        fields = (
            "in_box",
            "launched_date",
            "model_no",
            "model_name",
            "mobile",
            "laptop",
            "tv",
            "washing_machine",
            "ac",
            "refrigerator",
            "speaker",
        )


class ProductVariationSerializer(ModelSerializer):
    brand = BrandSerializer(many=False)
    seller = SellerUserSerializer(many=False)
    subcategory = ProductSubcategorySerializer(many=False)
    warranty = ProductWarranty(many=False)
    specification = ProductSpecification(many=False)

    class Meta:
        model = Product
        fields = (
            "brand",
            "name",
            "slug",
            "seller",
            "subcategory",
            "description",
            "overall_rating",
            "replacement_days",
            "warranty",
            "weight",
            "specification",
        )


class ProductVariationSerializer(ModelSerializer):

    product = ProductVariationSerializer(many=False)

    class Meta:
        model = ProductVariation
        fields = (
            "PID",
            "product",
            "retail_price",
            "price",
            "color",
            "available_stock",
            "mobile_variant",
            "laptop_variant",
            "tv_variant",
            "ac_capacity_variant",
            "refrigerator_capacity",
            "ac_star_variant",
            "book_variation",
            "juices_quantity",
            "size",
            "images",
        )
